import xml.etree.ElementTree as ET
import mwparserfromhell
import json
import argparse
import sys
import bz2
import subprocess
from typing import Optional

def clean_text(text):
    try:
        wikicode = mwparserfromhell.parse(text)
        # Remove external links
        for external_link in wikicode.filter_external_links():
            # Replace external link with its description or remove
            if external_link.title:
                wikicode.replace(external_link, str(external_link.title))
            else:
                wikicode.replace(external_link, '')
                    
        cleaned_text = wikicode.strip_code()
                    
        return cleaned_text
    
    except Exception as e:
        print(f"Unexpected error in clean_text: {e}")
        return None

def clean_html(text: str) -> Optional[str]:
    """
    WikitextをHTMLに変換します。
    ../mediawiki-services-parsoid/bin/parse.phpを使用して変換を行います。
    
    Args:
        text: 変換するWikitext
    Returns:
        変換されたHTML。エラーの場合はNone
    """
    try:
        # PHPスクリプトのパス
        php_script = "mediawiki-services-parsoid/bin/parse.php"
        
        # サブプロセスを作成し、標準入力/出力をパイプで接続
        process = subprocess.Popen(
            ["php", php_script],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # 入力テキストを送信し、結果を受け取る
        stdout, stderr = process.communicate(input=text)
        
        if process.returncode != 0:
            print(f"HTML変換エラー: {stderr}", file=sys.stderr)
            return None
            
        return stdout.strip()
        
    except Exception as e:
        print(f"HTML変換中に予期せぬエラーが発生: {e}", file=sys.stderr)
        return None

def is_valid_article(title, text, categories):
    # Skip articles with ':' (templates, categories, etc.)
    if ':' in title:
        return False
    
    # Skip list and disambiguation pages
    if "一覧" in title or "曖昧さ回避" in title:
        return False
    
    # If categories are specified, check if any match
    if categories:
        # Extract categories from the text
        wikicode = mwparserfromhell.parse(text)
        article_categories = [
            str(template).replace('[[Category:', '').replace(']]', '').strip()
            for template in wikicode.filter_templates()
            if str(template).startswith('[[Category:')
        ]
        
        # Check if any of the specified categories match
        if not any(cat in article_categories for cat in categories):
            return False
    
    return True

def extract_wikipedia_text(xml_file_path, output_file_path, max_articles=None, categories=None, start_index=0, language='ja'):
    articles = []
    article_count = 0

    with bz2.open(xml_file_path, 'rt', encoding='utf-8') as xml_file:
        context = ET.iterparse(xml_file, events=('end',))

        for _ in range(start_index):
            next(context)

        for event, elem in context:
            if elem.tag.endswith('page'):
                try:
                    title_elem = elem.find('{*}title')
                    text_elem = elem.find('.//{*}text')
                    
                    if title_elem is not None and text_elem is not None:
                        title = title_elem.text
                        text = text_elem.text
                        
                        if text and title and is_valid_article(title, text, categories):
                            cleaned_text = clean_text(text)
                            html_text = clean_html(text)

                            if cleaned_text is None or cleaned_text.startswith("REDIRECT"):
                                elem.clear()
                                continue
                            
                            articles.append({
                                'title': title,
                                'html': "<html><head><base href='https://" + language + ".wikipedia.org/wiki/'><title>" + title + "</title></head><body><h1>" + title + "</h1>" + html_text + "</body></html>"
                            })
                            
                            article_count += 1
                            
                            # Stop if max articles is reached
                            if max_articles and article_count >= max_articles:
                                break
                
                except Exception as e:
                    print(f"Error processing page: {e}", file=sys.stderr)
                
                elem.clear()

    # Write to JSON file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(articles, output_file, ensure_ascii=False, indent=2)
    
    print(f"Extracted {article_count} articles. Output saved to {output_file_path}")
    return article_count

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Extract Wikipedia articles from compressed XML dump')
    parser.add_argument('-i', '--input', 
                        default='jawiki-20241120-pages-articles-multistream.xml.bz2', 
                        help='Input compressed XML file path')
    parser.add_argument('-o', '--output', 
                        default='wikipedia_ja_extracted.json', 
                        help='Output JSON file path')
    parser.add_argument('-n', '--number', 
                        type=int,
                        default=100,
                        help='Maximum number of articles to extract')
    parser.add_argument('-c', '--categories', 
                        nargs='+', 
                        help='Categories to filter articles')
    parser.add_argument('-s', '--start', 
                        type=int,
                        default=0,
                        help='Start index of articles to extract')
    parser.add_argument('-l', '--language', 
                        default='ja',
                        help='Language of Wikipedia')

    # Parse arguments
    args = parser.parse_args()

    # Extract articles
    extract_wikipedia_text(
        args.input, 
        args.output, 
        max_articles=args.number, 
        categories=args.categories,
        start_index=args.start,
        language=args.language
    )

if __name__ == "__main__":
    main()