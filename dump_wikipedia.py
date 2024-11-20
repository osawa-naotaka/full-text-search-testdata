import requests

url = "https://ja.wikipedia.org/w/api.php"
headers = {'User-Agent': 'FTSTBot/1.0 (https://github.com/osawa-naotaka/full-text-search-testdata; ohsawa.naotaka@gmail.com)'}

def get_list():
    payload = {"format" : "json", "action" : "query", "list" : "random", "rnnamespace" : "0", "rnlimit" : "10"}
    response = requests.get(url, headers=headers, params=payload)
    dict = response.json()
    titles = map(lambda t: t['title'], dict['query']['random'])
    return list(titles)

def get_page(title):
    payload = {"format" : "php", "action" : "query", "prop" : "revisions", "rvprop" : "content", "rvslots": "main", "titles" : title}
    
    response = requests.get(url, headers=headers, params=payload)
    return '\n'.join(response.text.splitlines()[1:])

for title in get_list():
    content = get_page(title)
    print(title)
    print(content)
