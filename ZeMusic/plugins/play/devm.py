import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from ZeMusic import app
from config import OWNER_ID, LOGGER_ID


@app.on_message(command(["مطور", "‹ المطور ›", "المطور"]))
async def zdatsr(client: Client, message: Message):
    
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    photo = usr.photo.big_file_id
    photo = await client.download_media(photo)
    #await app.download_media(usr.photo.big_file_id, file_name=os.path.join("downloads", "developer.jpg"))
       
    await message.reply_photo(
        photo=photo,
        #photo="downloads/developer.jpg",
        caption=f"""<b>⌯ 𝙽𝙰𝙼𝙴 :</b> <a href="https://t.me/{usrnam}">{name}</a>

<b>⌯ 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 :</b> @{usrnam}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(name, url=f"https://t.me/{usrnam}"),
                ],[
                    InlineKeyboardButton(
                        "•✯  السورس  ✯•", url="https://t.me/terbo772"),
                ],
            ]
        ),
    )
    chat = message.chat.id
    gti = message.chat.title
    chatusername = f"@{message.chat.username}"
    link = await app.export_chat_invite_link(chat)
    user = await client.get_users(message.from_user.id)
    user_id = message.from_user.id
    user_ab = message.from_user.username
    user_name = message.from_user.first_name
    buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await app.send_message(OWNER_ID, f"<b>⌯ قام {message.from_user.mention}\n</b>"
                                     f"<b>⌯ بمناداتك عزيزي المطور\n</b>"
                                     f"<b>⌯ الأيدي {user_id}\n</b>"
                                     f"<b>⌯ اليوزر @{user_ab}\n</b>"
                                     f"<b>⌯ ايدي المجموعة {message.chat.id}\n</b>"
                                     f"<b>⌯ يوزر المجموعه {chatusername}</b>",
                                     reply_markup=reply_markup)

