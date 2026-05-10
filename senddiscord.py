import requests
import yaml
from score import open_config

config = open_config()

url = config['discord']['webhook_url']

def send_to_discord(result):
    preview = result['message'][:150]
    if len(preview) > 150:
        preview += '----------------------------'

    content = f"""**重要メールを確認しました**

**From:** {result['from']}
**件名:** {result['subject']}

**本文:**
{preview}

🔗 [Gmailで開く](https://mail.google.com/mail/u/0/#inbox/{result['id']})"""
    
    data = {
        "content": content,
        }

    try:
        response = requests.post(
            url, 
            json=data
        )
        
        if response.status_code == 204:
            print("Discord送信成功")
            return True
        else:
            print("Discord送信失敗")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"Webhook通信エラー: {e}")
        return False
    