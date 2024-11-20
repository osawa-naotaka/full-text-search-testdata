import requests
import json

url = "https://ja.wikipedia.org/w/api.php"
headers = {'User-Agent': 'FTSTBot/1.0 (https://github.com/osawa-naotaka/full-text-search-testdata; ohsawa.naotaka@gmail.com)'}

# Wikipediaのランダムな記事タイトルを取得する関数
def get_list():
    payload = {"format": "json", "action": "query", "list": "random", "rnnamespace": "0", "rnlimit": "100"}
    response = requests.get(url, headers=headers, params=payload)
    data = response.json()
    titles = map(lambda t: t['title'], data['query']['random'])
    return list(titles)

# 指定したタイトルの記事内容を取得する関数
def get_page(title):
    payload = {"format": "json", "action": "query", "prop": "revisions", "rvprop": "content", "rvslots": "main", "titles": title}
    response = requests.get(url, headers=headers, params=payload)
    data = response.json()
    
    pages = data['query']['pages']
    page_id = next(iter(pages))  # 取得された最初のページID
    revisions = pages[page_id].get('revisions')
    if revisions:
        return revisions[0]['slots']['main']['*']
    return ""

# メイン処理
def main():
    articles = []
    for title in get_list():
        content = get_page(title)
        articles.append({"title": title, "content": content})
    
    # JSON形式でファイルに保存
    with open("wikipedia_articles.json", "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
