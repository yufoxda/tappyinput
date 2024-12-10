import requests
from bs4 import BeautifulSoup

# ターゲットURL
url = "http://tap-py.com/aq49t2mn/register"  # 実際のURLに置き換えてください



response = requests.get(url)
if response.status_code == 200:
    # HTMLをパース
    soup = BeautifulSoup(response.text, "html.parser")
    
    datum = soup.find("table").find_all("tr")
    
    if not datum:
        print("can't found")
        exit()
        
    dates_text = datum[0].get_text()
    dates = list(dates_text.split())

    times = []
    dates_id = []
    time_id = []
    for i in range(1,len(datum)):
        times.append(datum[i].find("th").get_text())
        time_id.append(datum[i].find("input").get("value"))

    input_fields = datum[i].find_all("input")
    num = 0
    for j in input_fields:
       
        print(j.get("name"),j.get("value"))
        if (num)%4 == 1:
            dates_id.append(j.get("value"))
        # times.append(j.get("name"))
        num+=1


    test = {}

    print(times)
    print(time_id)
    print(dates)
    print(dates_id)

else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")




import requests
from bs4 import BeautifulSoup

# フォームのURL
url = "http://tap-py.com/cco6k7ao/register"  # 実際のフォームURLに変更してください

# フォームに送信するデータ
form_data = {
    "data[Attendance][0][board_row_id]": "3336604",
    "data[Attendance][0][board_column_id]": "2857816",
    "data[Attendance][0][is_valied]": "1",  # チェックボックスにチェックを入れる場合

    "data[Member][name]": "yu",  # パスワード
    "data[Member][password]": "password123",  # パスワード
    "data[Comment][body]": "自動入力です",  # コメント
}



# ヘッダーの設定
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",  # フォームデータを送信する形式
}

# POSTリクエストを送信
response = requests.post(url, data=form_data, headers=headers)

# レスポンスの確認
if response.status_code == 200:
    print(response.text)
    print("フォームの送信が成功しました！")
else:
    print(f"エラーが発生しました: {response.status_code}")
