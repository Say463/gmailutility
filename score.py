import yaml

def open_config():
    with open('config.yaml','r',encoding="utf-8") as yml:
        config = yaml.safe_load(yml)
        return config

def scoring(result,config):
    score = 0
    mail_text = (result['message'] + result['subject'])
    from_adress = result['from']

    for text,weight in config['scoring']['keywords'].items():
        if text in mail_text:
            score += weight
    return score




