import asyncio
import streamlit as st

import msg
from bilibili import newmsg
import gpt
import re
import loadconfig

def extract_content(input_str):
    pattern = r'^画(.+)$'
    match = re.match(pattern, input_str)
    if match:
        return match.group(1)
    return None

async def getmsg(roomid):
    while True:
        try:
            if st.session_state.connected:
                pass
        except:
            break
        global data
        newmsgdata= newmsg(roomid, data.lastid())
        data.add(newmsgdata)
        data.lastid()
        if newmsgdata!=None:
            await asyncio.sleep(1)
        else:
            await asyncio.sleep(5)

async def AI():
    global data, lable
    GPT=gpt.gpt()
    GPT.keyinfo()
    run=True
    while run:
        while data.head != None and run==True:
            try:
                if st.session_state.connected:
                    pass
            except:
                run=False
                break
            label.table(data.todict())
            user_input = data.head.msg.text
            user = st.empty()
            user.info(data.head.msg.uname + "：" + data.head.msg.text)
            ai = st.empty()
            if extract_content(user_input) != None:
                response = GPT.draw(extract_content(user_input))
                ai.image(response)
            else:
                response = GPT.completion(user_input)
                ai.success("AI：" + response)
            data.head = data.head.next
            await asyncio.sleep(10)
            while data.head == None:
                await asyncio.sleep(1)
            user.empty()
            ai.empty()
        label.table(data.todict())
        await asyncio.sleep(1)
async def main():
    global data, label
    data = msg.msgList()
    data.head = None
    st.sidebar.title("人工智障")
    st.sidebar.success("使用说明:\n\n#开头的消息会被回复 例如：#你是谁\n\n#画开头的消息会被画出来 例如：#画一只猫")

    roomid = st.sidebar.number_input("roomid", min_value=0, max_value=100000000,value=loadconfig.roomid())
    button = st.sidebar.button("start")
    label = st.sidebar.table()
    if button:
        st.session_state.connected = True
        task=asyncio.create_task(getmsg(roomid))
        task2=asyncio.create_task(AI())
        await task
        await task2
if __name__ == "__main__":
    asyncio.run(main())
