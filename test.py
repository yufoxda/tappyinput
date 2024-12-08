import requests
from bs4 import BeautifulSoup

# ターゲットURL
url = "http://tap-py.com/aq49t2mn/register"  # 実際のURLに置き換えてください

# 必要であればCookieやヘッダーを指定
cookies = {
    "tappy": "aa1365944b006525658ffb84b738d39b"  # 必要ならクッキー値を設定
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# ページを取得
response = requests.get(url, cookies=cookies, headers=headers)
if response.status_code == 200:
    # HTMLをパース
    soup = BeautifulSoup(response.text, "html.parser")
    
    # class="TappyTable RenderVerticalPressed" の<table>を取得
    table = soup.find("table")
    
    if table:
        
        # 最初の<tr>を取得
        first_tr = table.find("tr")
        if first_tr:
            
            text = first_tr.get_text()  # strip=Trueで前後の空白を除去
            print(text)
            word_count = len(text.split())  # テキストをスペースで分割したリストの長さを取得
            print("Word count in the first <tr>:", word_count)
        else:
            print("No <tr> found in <tbody>.")
    else:
        print("Table not found.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")