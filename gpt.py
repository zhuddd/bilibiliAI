import datetime
import json

import requests
from loadconfig import url, key


class gpt:

    def __init__(self):
        self.messages = []

    def getmodel(self):
        head = {
            "Authorization": f'Bearer {key()}'
        }
        response = requests.get(url() + "/models", headers=head)
        if response.status_code != 200:
            return json.loads(response.text)
        elif response.status_code == 200:
            return json.loads(response.text)

    def msg(self, role, content):
        messages = {
            "role": role,
            "content": content
        }
        self.messages.append(messages)

    def completion(self, content):
        self.msg("user", content)
        data = {
            "model": "gpt-3.5-turbo",
            "messages": self.messages,
            "temperature": 1,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {key()}'
        }
        response = requests.post(url() + "/chat/completions", headers=headers, json=data)
        if response.status_code != 200:
            return json.loads(response.text)
        elif response.status_code == 200:
            answer = json.loads(response.text)['choices'][0]['message']['content']
            self.msg("system", answer)
            return answer

    def draw(self, content):
        data = {
            "prompt": content,
            "n": 1,
            "size": "1024x1024"
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {key()}'
        }
        response = requests.post(url() + "/images/generations", headers=headers, json=data)
        if response.status_code != 200:
            return json.loads(response.text)
        elif response.status_code == 200:
            answer = json.loads(response.text)['data'][0]['url']
            return answer

    def keyinfo(self):
        apikey = key()
        subscription_url = url() + "/dashboard/billing/subscription"
        headers = {
            "Authorization": "Bearer " + apikey,
            "Content-Type": "application/json"
        }
        subscription_response = requests.get(subscription_url, headers=headers)
        if subscription_response.status_code == 200:
            data = subscription_response.json()
            total = data.get("hard_limit_usd")
            access_until = data.get("access_until")
            print("账户额度:" + str(total))
            print("有效期:" + datetime.datetime.fromtimestamp(access_until).strftime('%Y-%m-%d %H:%M:%S'))
        else:
            print(subscription_response.text)
