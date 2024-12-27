import requests
import schedule
import time

# LINE Messaging APIの設定
LINE_ACCESS_TOKEN = "<ptIKcB/wz28ugFmuDZZivZFX/aYaSpGlt4FpMv8VASVe4P9lIfFYSTSTkJDzI1H8qJyqzayp1ENDFkzSj5Y4G6ud6gKlx+fcXHfdWcUrpVgK0p+++FJZ/ySgTqGsubZEylw3mV3pA8r/zQEzVbNU2AdB04t89/1O/w1cDnyilFU=>"  # LINE公式アカウントのアクセストークンをここに記述

# メッセージ送信関数
def send_line_message():
    url = "https://api.line.me/v2/bot/message/broadcast"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}"
    }
    data = {
        "messages": [
            {
                "type": "text",
                "text": "＜サーバー名＞は現在稼働中"
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("メッセージ送信成功")
    else:
        print(f"メッセージ送信失敗: {response.status_code} - {response.text}")

# 毎日14時にメッセージを送信するスケジュールを設定
schedule.every().day.at("14:00").do(send_line_message)

print("スケジュールを開始します...")

# スケジュール実行ループ
while True:
    schedule.run_pending()
    time.sleep(1)
