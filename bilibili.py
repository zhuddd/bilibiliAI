import json
import aiohttp
import msg
import re

async def extract_content(text):
    pattern = r'^#(.+)$'
    match = re.match(pattern, text)
    if match:
        return match.group(1)
    return None

async def getmsg(roomid):
    url = "http://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid=" + str(roomid) + "&room_type=1"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            res = await response.json()
            d = res['data']['room']
            data = msg.msgList()
            data.head = None
            try:
                for i in range(len(d)):
                    content = d[i]['text']
                    matched_content = await extract_content(content)
                    if matched_content is not None:
                        data.add(msg.node(msg.msg(matched_content, d[i]['nickname'], d[i]['uid'], d[i]['id_str'])))
                return data
            except:
                return data

async def findnode(data, id):
    p = data.head
    while p != None:
        if p.msg.id == id:
            return p.next
        p = p.next
    return data.head

async def newmsg(roomid, id):
    return await findnode(await getmsg(roomid), id)
