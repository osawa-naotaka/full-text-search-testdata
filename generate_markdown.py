import json
import os
import argparse
from pathlib import Path

def sanitize_filename(title):
    """ファイル名として使用できない文字を置換する"""
    # Windows/Unix両方で使用できない文字を置換
    invalid_chars = '<>():"/\\|?*'
    filename = title
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    filename = filename.replace(' ', '_')
    return filename

def generate_markdown_files(json_file_path, output_dir):
    """JSONファイルからmarkdownファイルを生成する"""
    # 出力ディレクトリが存在しない場合は作成
    os.makedirs(output_dir, exist_ok=True)
    
    # JSONファイルを読み込む
    with open(json_file_path, 'r', encoding='utf-8') as f:
        articles = json.load(f)
    
    # 各記事についてmarkdownファイルを生成
    for article in articles:
        title = article['title']
        text = article['text']
        
        # ファイル名を生成（タイトルから不正な文字を除去）
        filename = sanitize_filename(title) + '.md'
        filepath = os.path.join(output_dir, filename)
        
        # markdownファイルを作成
        with open(filepath, 'w', encoding='utf-8') as f:
            # ヘッダー情報を追加
            f.write(f'---\ntitle: {title}\n---\n')
            # 本文を追加
            f.write(text)
        
        print(f'Generated: {filepath}')

def main():
    parser = argparse.ArgumentParser(description='Generate markdown files from Wikipedia JSON')
    parser.add_argument('-i', '--input',
                      default='wikipedia_ja_extracted.json',
                      help='Input JSON file path')
    parser.add_argument('-o', '--output',
                      default='markdown_output',
                      help='Output directory for markdown files')
    
    args = parser.parse_args()
    
    generate_markdown_files(args.input, args.output)

if __name__ == "__main__":
    main() 