import xml.etree.ElementTree as ET
import mwparserfromhell
import json
import argparse
import sys
import bz2

def extract_wikipedia_text(xml_file_path, output_file_path, max_articles=None, categories=None, start_index=0):
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

                            if cleaned_text is None or cleaned_text.startswith("REDIRECT"):
                                elem.clear()
                                continue
                            
                            articles.append({
                                'title': title,
                                'text': cleaned_text
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

    # Parse arguments
    args = parser.parse_args()

    # Extract articles
    extract_wikipedia_text(
        args.input, 
        args.output, 
        max_articles=args.number, 
        categories=args.categories,
        start_index=args.start
    )

if __name__ == "__main__":
    main()