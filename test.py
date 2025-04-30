import urllib.request
import json

url = "https://92b6-35-223-26-60.ngrok-free.app/generate"
payload = {
    "prompt": "日本の首都は？"
}

# JSONデータをエンコード
data = json.dumps(payload).encode("utf-8")

# リクエストオブジェクトを作成
req = urllib.request.Request(
    url,
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST"
)

# リクエストを送信してレスポンスを取得
with urllib.request.urlopen(req) as res:
    response_body = json.loads(res.read().decode("utf-8"))

# レスポンスを解析
print("Bedrock response:", json.dumps(response_body, default=str))