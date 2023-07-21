import datetime
from configparser import ConfigParser

import json
def url():
    config = ConfigParser()
    config.read('config.cfg',encoding='utf-8')
    if config['openAI']['url'] == '':
        return 'http://api.openai.com/v1'
    else:
        return config['openAI']['url']

def key():
    config = ConfigParser()
    config.read('config.cfg',encoding='utf-8')
    if config['openAI']['apiKey'] == '':
        return None
    else:
        return config['openAI']['apiKey']

def roomid():
    config = ConfigParser()
    config.read('config.cfg',encoding='utf-8')
    if config['bilibili']['roomid'] == '':
        return None
    else:
        id=config['bilibili']['roomid']
        return int(id)


