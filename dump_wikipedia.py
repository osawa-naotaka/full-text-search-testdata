import requests
import sys
import time
import re
from typing import Dict, List
import subprocess
from typing import Optional
import urllib.parse


if(len(sys.argv) != 2):
    exit(-1)

lang_code = sys.argv[1]
url = "https://{}.wikipedia.org/w/api.php".format(lang_code)
print(url)

headers = {'User-Agent': 'FTSTBot/1.0 (https://github.com/osawa-naotaka/full-text-search-testdata; ohsawa.naotaka@gmail.com)'}

# 言語ごとの設定
LANGUAGE_CONFIGS = {
    "ja": {
        "min_length": 2000,
        "target_ratio": 0.3,
        "exclude_categories": ["一覧", "スタブ", "曖昧さ回避"],
        "script_pattern": r'[ぁ-んァ-ン一-龥]+',
    },
    "en": {
        "min_length": 2000,
        "target_ratio": 0.5,
        "exclude_categories": ["Lists", "Stub", "Disambiguation"],
        "script_pattern": r'[a-zA-Z]+',
    },
    "zh": {
        "min_length": 1500,
        "target_ratio": 0.3,
        "exclude_categories": ["列表", "小作品", "消歧义"],
        "script_pattern": r'[\u4e00-\u9fff]+',
    },
    "ko": {
        "min_length": 1500,
        "target_ratio": 0.3,
        "exclude_categories": ["목록", "토막글", "동음이의"],
        "script_pattern": r'[\uac00-\ud7af\u1100-\u11ff]+',
    },
    # 他の言語も同様に追加可能
}

def get_language_config():
    """言語設定を取得。未定義の言語の場合はデフォルト設定を返す"""
    default_config = {
        "min_length": 2000,
        "target_ratio": 0.4,
        "exclude_categories": ["Stub", "List", "Disambiguation"],
        "script_pattern": None,  # 未定義の言語はlangdetectに依存
    }
    return LANGUAGE_CONFIGS.get(lang_code, default_config)

def get_list():
    payload = {"format": "json", "action": "query", "list": "random", "rnnamespace": "0", "rnlimit": "100"}
    response = requests.get(url, headers=headers, params=payload)
    if(response.status_code != 200):
        print("error response {} at get_page".format(response.status_code))
        exit(-1)
    data = response.json()
    titles = map(lambda t: t['title'], data['query']['random'])
    return list(titles)

def get_page(title):
    payload = {
        "format": "json",
        "action": "query",
        "prop": "revisions|categories",
        "rvprop": "content",
        "rvslots": "main",
        "titles": title,
        "cllimit": "50"
    }
    response = requests.get(url, headers=headers, params=payload)
    if(response.status_code != 200):
        print("error response {} at get_page".format(response.status_code))
        exit(-1)
    data = response.json()
    
    pages = data['query']['pages']
    page_id = next(iter(pages))
    page_data = pages[page_id]
    
    revisions = page_data.get('revisions')
    if not revisions:
        return None
        
    content = wiki_to_markdown(revisions[0]['slots']['main']['*'])
    categories = page_data.get('categories', [])
    return {'content': content, 'categories': categories}


def is_quality_article(page_data: Dict) -> bool:
    if not page_data:
        return False
    
    config = get_language_config()
    content = page_data['content']
    categories = page_data['categories']

    if not content or not categories:
        return False
    
    # 記事の長さチェック
    if len(content) < config["min_length"]:
        return False
    
    # カテゴリーチェック
    for category in categories:
        cat_title = category.get('title', '')
        if any(ex_cat in cat_title for ex_cat in config["exclude_categories"]):
            return False
    

def wiki_to_markdown(text: str) -> Optional[str]:
    try:
        process = subprocess.Popen(
            ["pandoc", "-f", "mediawiki", "-t", "markdown"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # 入力テキストを送信し、結果を受け取る
        stdout, stderr = process.communicate(input=text)
        
        if process.returncode != 0:
            print(f"markdown変換エラー: {stderr}", file=sys.stderr)
            return None
            
        return stdout.strip()
        
    except Exception as e:
        print(f"markdown変換中に予期せぬエラーが発生: {e}", file=sys.stderr)
        return None

def main():
    articles = []
    processed_count = 0
    target_count = 10
    
    while len(articles) < target_count and processed_count < 1000:
        titles = get_list()
        for title in titles:
            page_data = get_page(title)
            # if is_quality_article(page_data):
            # フロントマターを追加
            content_with_front_matter = f"---\ntitle: {title}\n---\n{page_data['content']}"
            
            # URLエンコードされたファイル名を生成
            encoded_title = urllib.parse.quote(title)
            file_path = f"md/{encoded_title}.md"
            
            # ファイルに保存
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content_with_front_matter)
            
            print(f"Saved quality article: {title} to {file_path}")
            
            processed_count += 1
            if processed_count >= target_count:
                break
            
            time.sleep(1)
        
        if processed_count < target_count:
            print(f"Processed {processed_count} articles so far, continuing search...")
    
    print(f"Processed {processed_count} articles to find {target_count} quality articles")

if __name__ == "__main__":
    main()
