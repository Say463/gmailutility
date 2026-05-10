import quickstart
import acquision
import score
import yaml
from senddiscord import send_to_discord

service = quickstart.gmail_init()

messages = acquision.gmail_message_list(['INBOX'],10,query="is:unread")

config = score.open_config()


for msg in messages:
    result = acquision.get_message_detail(msg['id'])
    if not result:
        continue
    
    points = score.scoring(result,config)
    if points >= config['notifier']['threshold']:
        send_to_discord(result)

    acquision.add_remove_label(msg['id'],["IMPORTANT"],["UNREAD"])
    

    
print("チェック完了")