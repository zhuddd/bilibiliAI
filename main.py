import time

import bilibili
import gpt
import loadconfig as lc
import msg
import web_app
import asyncio


async def main():
    await chatgpt.init()
    task = asyncio.create_task(updateData(newApp.roomID))
    task2 = asyncio.create_task(aioutput())
    await task
    await task2


async def updateData(roomID):
    while newApp.is_connected():
        new = await bilibili.newmsg(roomID, data.lastid())
        data.add(new)
        data.lastid()
        newApp.set_user_table(data.todict())
        if new is not None:
            await asyncio.sleep(1)
        else:
            await asyncio.sleep(2)
    print("msg stopped")


async def aioutput():
    while newApp.is_connected():
        while data.head is not None and newApp.is_connected():
            newApp.set_user_table(data.todict())
            newApp.clean_conversation()
            newApp.set_user_conversation(data.head.msg.uname, data.head.msg.text)
            await answer(data.head.msg.text)
            data.head = data.head.next
            await asyncio.sleep(10)
            while data.head is None and newApp.is_connected():
                await asyncio.sleep(1)
        await asyncio.sleep(1)
    print("ai stopped")


async def answer(msg):
    if msg.startswith("重置"):
        await chatgpt.clear()
        newApp.set_ai_conversation("重置成功")
        return
    if msg.startswith("回溯"):
        newApp.set_ai_conversation("暂不支持")
        return
    if msg.startswith("画"):
        newApp.set_ai_image(await chatgpt.draw(msg))
    else:
        newApp.set_ai_conversation(await chatgpt.completion(msg))


newApp = web_app.App()
data = msg.msgList()
chatgpt = gpt.gpt()
if __name__ == '__main__':
    newApp.set_title(lc.title())
    newApp.set_notice(lc.notice())
    newApp.set_roomID(lc.roomid())
    if newApp.start:
        asyncio.run(main())
