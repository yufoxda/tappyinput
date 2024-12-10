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
