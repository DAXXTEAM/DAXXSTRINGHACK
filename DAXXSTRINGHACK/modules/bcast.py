from pyrogram import filters
from config import Config

from DAXXSTRINGHACK import app
from DAXXSTRINGHACK.Helpers.mongo import get_served_chats
from DAXXSTRINGHACK.Helpers.mongo import get_served_users

IS_BROADCASTING = False
SUDOERS = Config.SUDOERS


@app.on_message(filters.command(["broadcast", "gcast", "bcast"]) & SUDOERS)
async def braodcast_message(client, message):
    global IS_BROADCASTING
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text("**Usage**:\n/broadcast [MESSAGE] or [Reply to a Message]")
        query = message.text.split(None, 1)[1]
        if "-pin" in query:
            query = query.replace("-pin", "")
        if "-nobot" in query:
            query = query.replace("-nobot", "")
        if "-pinloud" in query:
            query = query.replace("-pinloud", "")
        if "-user" in query:
            query = query.replace("-user", "")
        if query == "":
            return await message.reply_text("Please provide some text to broadcast.")

    IS_BROADCASTING = True

    # Bot broadcast inside chats
    if "-nobot" not in message.text:
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            if i == -1001733534088:
                continue
            try:
                m = (
                    await app.forward_messages(i, y, x)
                    if message.reply_to_message
                    else await app.send_message(i, text=query)
                )
                if "-pin" in message.text:
                    try:
                        await m.pin(disable_notification=True)
                        pin += 1
                    except Exception:
                        continue
                elif "-pinloud" in message.text:
                    try:
                        await m.pin(disable_notification=False)
                        pin += 1
                    except Exception:
                        continue
                sent += 1
            except FloodWait as e:
                flood_time = int(e.x)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except Exception:
                continue
        try:
            await message.reply_text("**Broadcasted Message In {0}  Chats with {1} Pins from Bot.**".format(sent, pin))
        except:
            pass

    # Bot broadcasting to users
    if "-user" in message.text:
        susr = 0
        served_users = []
        susers = await get_served_users()
        for user in susers:
            served_users.append(int(user["user_id"]))
        for i in served_users:
            try:
                m = (
                    await app.forward_messages(i, y, x)
                    if message.reply_to_message
                    else await app.send_message(i, text=query)
                )
                susr += 1
            except FloodWait as e:
                flood_time = int(e.x)
                if flood_time > 200:
                    continue
                await asyncio.sleep(flood_time)
            except Exception:
                pass
        try:
            await message.reply_text("**Broadcasted Message to {0} Users.**".format(susr))
        except:
            pass
    IS_BROADCASTING = False

