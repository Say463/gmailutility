import quickstart
import acquision
import score
import yaml
from senddiscord import send_to_discord

service = quickstart.gmail_init()

config = score.open_config()

messages = acquision.gmail_message_list(['INBOX'],config['notifier']['max_check'],query="is:unread")


for msg in messages:
    result = acquision.get_message_detail(msg['id'])
    if not result:
        continue
    
    points = score.scoring(result,config)
    if points >= config['notifier']['threshold']:
        send_to_discord(result)

    


    
print("チェック完了")