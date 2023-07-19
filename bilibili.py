import json
import requests
import msg
import re

def extract_content(text):
    pattern = r'^#(.+)$'
    match = re.match(pattern, text)
    if match:
        return match.group(1)
    return None
def getmsg(roomid):
    url = "http://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory?roomid="+str(roomid)+"&room_type=1"
    res = requests.get(url=url)
    d=json.loads(res.text)
    d=d['data']['room']
    data = msg.msgList()
    data.head = None
    try:

        for i in range(len(d)):
            content = d[i]['text']
            matched_content = extract_content(content)
            if matched_content is not None:
                data.add(msg.node(msg.msg(matched_content, d[i]['nickname'], d[i]['uid'], d[i]['id_str'])))
        return data
    except:
        return data

def findnode(data, id):
    p=data.head
    while p!=None:
        if p.msg.id==id:
            return p.next
        p=p.next
    return data.head
def newmsg(roomid,id):
    return findnode(getmsg(roomid),id)




