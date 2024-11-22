import requests
import json
import sys
import time

if(len(sys.argv) != 2) :
    exit(-1)

url = "https://{}.wikipedia.org/w/api.php".format(sys.argv[1])
print(url)

headers = {'User-Agent': 'FTSTBot/1.0 (https://github.com/osawa-naotaka/full-text-search-testdata; ohsawa.naotaka@gmail.com)'}

# Wikipediaのランダムな記事タイトルを取得する関数
def get_list():
    payload = {"format": "json", "action": "query", "list": "random", "rnnamespace": "0", "rnlimit": "100"}
    response = requests.get(url, headers=headers, params=payload)
    if(response.status_code != 200):
        print("error response {} at get_page".format(response.status_code))
        exit(-1)
    data = response.json()
    titles = map(lambda t: t['title'], data['query']['random'])
    return list(titles)

# 指定したタイトルの記事内容を取得する関数
def get_page(title):
    payload = {"format": "json", "action": "query", "prop": "revisions", "rvprop": "content", "rvslots": "main", "titles": title}
    response = requests.get(url, headers=headers, params=payload)
    if(response.status_code != 200):
        print("error response {} at get_page".format(response.status_code))
        exit(-1)
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
        time.sleep(1)
        
    
    # JSON形式でファイルに保存
    with open("wikipedia_articles.{}.json".format(sys.argv[1]), "w", encoding="utf-8") as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()
