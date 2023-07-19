import asyncio
import streamlit as st

import msg
from bilibili import newmsg
from gpt import ChatGPT_AI_DrawBot, generate_response
import re


def extract_content(input_str):
    pattern = r'^画(.+)$'
    match = re.match(pattern, input_str)
    if match:
        return match.group(1)
    return None

async def getmsg(roomid):
    while True:
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
    context = ""
    while True:
        while data.head != None:
            label.table(data.todict())
            user_input = data.head.msg.text
            user = st.empty()
            user.info(data.head.msg.uname + "：" + data.head.msg.text)
            ai = st.empty()
            context = context + user_input + "\n"

            if extract_content(user_input) != None:
                response = ChatGPT_AI_DrawBot(extract_content(user_input))
                ai.image(response)
            else:
                response = generate_response(context)
                ai.success("AI：" + response)
            context = context + response + "\n"
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
    st.sidebar.info("使用说明：")
    st.sidebar.info("#开头的消息会被回复 例如：#你是谁")
    st.sidebar.info("#画开头的消息会被画出来 例如：#画一只猫")

    roomid = st.sidebar.number_input("roomid", min_value=0, max_value=100000000)
    button = st.sidebar.button("start")
    label = st.sidebar.table()
    if button:
        task=asyncio.create_task(getmsg(roomid))
        task2=asyncio.create_task(AI())
        await task
        await task2
if __name__ == "__main__":
    asyncio.run(main())
