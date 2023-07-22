import datetime
from configparser import ConfigParser, SafeConfigParser
from configparser import RawConfigParser
def url():
    try:
        config = ConfigParser()
        config.read('config.cfg', encoding='utf-8')
        if config['openAI']['url'] != '':
            return config['openAI']['url']
        else:
            return 'http://api.openai.com/v1'
    except:
        return 'http://api.openai.com/v1'


def key():
    try:
        config = ConfigParser()
        config.read('config.cfg', encoding='utf-8')
        return config['openAI']['apiKey']
    except:
        return None


def roomid():
    try:
        config = ConfigParser()
        config.read('config.cfg', encoding='utf-8')
        id = config['bilibili']['roomid']
        return int(id)
    except:
        return None
def title():
    try:
        config = ConfigParser()
        config.read('config.cfg', encoding='utf-8')
        return str(config['app']['title'])
    except:
        return None

def notice():
    try:
        config = ConfigParser()
        config.read('config.cfg', encoding='utf-8')
        return replacedstr(config['app']['notice'])
    except :
        return None
def replacedstr(input_str):
    replaced_str = input_str.replace('\\n', '\n')
    return replaced_str

