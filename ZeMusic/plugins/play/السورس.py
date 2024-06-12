import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint
import config
                
@app.on_message(
    command(["سورس","‹ السورس ›"," ","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/a31f8a9d92459aa707b4c.jpg",
        caption = f"""<b>  ⌯ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 . .<br>
        <a href="https://t.me/terbo772"> ⌯ 𝚂𝙾𝚄𝚁𝙲𝙴 𝚃𝙴𝚁𝙱𝙾 ⛧</a></b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="‹ لتنصيب بوت ›", url=f"https://t.me/VP_AB"),
                ],[
                    InlineKeyboardButton(
                        text=config.SURS_NAME, url=config.SUPPORT_CHANNEL),
                ],

            ]

        ),

    )
