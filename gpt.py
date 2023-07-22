import datetime
import json
import aiohttp
import asyncio
from loadconfig import url, key


class gpt:

    def __init__(self):
        self.messages = []

    async def fetch(self, session, url, headers=None, data=None, method='GET'):
        async with session.request(method, url, headers=headers, json=data) as response:
            return await response.json()

    async def getmodel(self):
        head = {
            "Authorization": f'Bearer {key()}'
        }
        async with aiohttp.ClientSession() as session:
            response = await self.fetch(session, url() + "/models", headers=head)
            return response

    async def msg(self, role, content):
        messages = {
            "role": role,
            "content": content
        }
        self.messages.append(messages)

    async def completion(self, content):
        await self.msg("user", content)
        data = {
            "model": "gpt-3.5-turbo",
            "messages": self.messages,
            "temperature": 1,
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {key()}'
        }
        async with aiohttp.ClientSession() as session:
            response = await self.fetch(session, url() + "/chat/completions", headers=headers, data=data, method='POST')
            try:
                answer = response['choices'][0]['message']['content']
                await self.msg("system", answer)
                return answer
            except:
                return response

    async def draw(self, content):
        data = {
            "prompt": content,
            "n": 1,
            "size": "1024x1024"
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f'Bearer {key()}'
        }
        async with aiohttp.ClientSession() as session:
            response = await self.fetch(session, url() + "/images/generations", headers=headers, data=data, method='POST')
            try:
                answer = response['data'][0]['url']
                return answer
            except:
                return response


    async def keyinfo(self):
        apikey = key()
        subscription_url = url() + "/dashboard/billing/subscription"
        headers = {
            "Authorization": "Bearer " + apikey,
            "Content-Type": "application/json"
        }
        async with aiohttp.ClientSession() as session:
            subscription_response = await self.fetch(session, subscription_url, headers=headers)
            try:
                if subscription_response['plan']['id']=="free":
                    print("当前套餐：免费版")
                    print("额度",subscription_response['hard_limit_usd'])
            except:
                print("error")

    async def init(self):
        if key() is None:
            print("请先设置apikey")
            return
        await self.keyinfo()

    async def clear(self):
        self.messages = []

