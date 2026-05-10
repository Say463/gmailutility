import os 
import base64
import quickstart 
from googleapiclient.errors import HttpError

service = quickstart.gmail_init()

#labelIdsValueのメールのIDを取得。
def gmail_message_list(labelValue,limit,query):
    try:
        message_list = service.users().messages().list(
        userId = 'me',labelIds=labelValue,maxResults = limit,q=query).execute()
        newmessage = message_list.get('messages',[])
        if message_list['resultSizeEstimate'] == 0:
            print("No emails match your criteria")
        
        return newmessage
    except HttpError as error:
        print(f'action=get_mail_list error={error}')
        return []    
    



#idから本文取得
def get_message_detail(msg_id):
        try:
            message = service.users().messages().get(userId = "me",id = msg_id,format = 'full').execute()
            payload = message['payload']
            body = decode(payload)
        except HttpError as error:
            print(f'action=get_message error={error}')
            
        result = {}
        headers = message['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'].lower() == 'subject'), '件名なし')
        from_address = next((h['value'] for h in headers if h['name'].lower() == 'from'), '送信者不明')

        result['id'] = msg_id
        result['subject'] = subject
        result['from'] = from_address
        result['message'] = body

        return result
     

def decode(payload):
        body = ""
        def subdecode(parts):
            nonlocal body
            data = parts.get('body',{}).get('data')
            mimetype = parts.get("mimeType","")
            if mimetype == 'text/plain' and data:
                decord = base64.urlsafe_b64decode(data).decode("utf-8",errors = 'ignore')
                body += decord
            elif mimetype == "text/html" and data:
                decord = base64.urlsafe_b64decode(data).decode("utf-8",errors = 'ignore')
                body += decord

        if 'parts' in payload:
            for part in payload['parts']:
                subdecode(part)
        else:
            subdecode(payload)

        return body


messages = gmail_message_list(labelValue=['INBOX'], limit=5, query="is:unread")
    

    


    




    



