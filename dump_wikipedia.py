import requests
import json
import sys
import time
import re
from typing import Dict, List
import unicodedata
import langdetect  # 追加のライブラリが必要

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
        
    content = revisions[0]['slots']['main']['*']
    categories = page_data.get('categories', [])
    return {'content': content, 'categories': categories}

def check_language_content(content: str, config: Dict) -> bool:
    """言語固有の文字や表現の含有率をチェック"""
    if config["script_pattern"]:
        # 言語固有の文字パターンが定義されている場合
        script_matches = re.findall(config["script_pattern"], content)
        script_char_count = sum(len(text) for text in script_matches)
        total_content_length = len(content)
        return script_char_count >= total_content_length * config["target_ratio"]
    else:
        # 未定義の言語の場合はlangdetectを使用
        try:
            detected_lang = langdetect.detect(content)
            return detected_lang == lang_code
        except:
            return False

def clean_content(content: str) -> str:
    """ウィキテキストから実際のテキスト内容を抽出"""
    # 基本的なウィキマークアップの除去
    content = re.sub(r'\{\{[^\}]*\}\}', '', content)  # テンプレートの除去
    content = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', content)  # リンクの除去
    content = re.sub(r'==.*?==', '', content)  # 見出しの除去
    content = re.sub(r'<ref>.*?</ref>', '', content)  # 参照の除去
    return content

def is_quality_article(page_data: Dict) -> bool:
    if not page_data:
        return False
    
    config = get_language_config()
    content = page_data['content']
    categories = page_data['categories']
    
    # 記事の長さチェック
    if len(content) < config["min_length"]:
        return False
    
    # カテゴリーチェック
    for category in categories:
        cat_title = category.get('title', '')
        if any(ex_cat in cat_title for ex_cat in config["exclude_categories"]):
            return False
    
    # クリーンなテキストを取得
    clean_text = clean_content(content)
    
    # 言語チェック
    if not check_language_content(clean_text, config):
        return False
    
    # テンプレートや整形式の多用をチェック
    template_count = content.count('{{')
    text_length = len(content)
    if template_count > text_length / 200:
        return False
    
    # 箇条書きの割合をチェック
    bullet_points = content.count('*') + content.count('#')
    if bullet_points > text_length / 50:
        return False
    
    return True

def main():
    articles = []
    processed_count = 0
    target_count = 100
    
    while len(articles) < target_count and processed_count < 1000:
        titles = get_list()
        for title in titles:
            page_data = get_page(title)
            if is_quality_article(page_data):
                articles.append({
                    "title": title,
                    "content": page_data['content']
                })
                print(f"Found quality article: {title}")
                if len(articles) >= target_count:
                    break
            
            processed_count += 1
            time.sleep(1)
        
        if len(articles) < target_count:
            print(f"Found {len(articles)} quality articles so far, continuing search...")
    
    # JSON形式でファイルに保存
    with open("wikipedia_articles.{}.json".format(lang_code), "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)
    
    print(f"Processed {processed_count} articles to find {len(articles)} quality articles")

if __name__ == "__main__":
    main()
