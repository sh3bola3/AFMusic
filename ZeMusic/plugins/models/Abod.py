import asyncio
import re
import os
import time
import requests
from config import START_IMG_URL, BOT_NAME
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

Nb = BOT_NAME + " غنيلي"

@app.on_message(filters.regex(r"^(غنيلي|‹ غنيلي ›|" + re.escape(Nb) + r")$"))
async def ihd(client: Client, message: Message):
    rl = random.randint(2, 90)
    url = f"https://t.me/BE_19/{rl}"
    await client.send_voice(
        chat_id=message.chat.id,
        voice=url,
        caption="↯ : تم اختيار اغنية لك 🤍",
        reply_to_message_id=message.id,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=message.from_user.first_name,
                        url="https://t.me/terbo772"
                    )
                ],
            ]
        )
    )



@app.on_message(command(["‹ صور ›","صور"]) & filters.private)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯ : تم اختيار صوره اليك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/terbo772")
                ],
            ]
        )
    )


@app.on_message(command(["‹ انمي ›", "انمي"]) & filters.private)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯ : تم اختيار انمي اليك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/terbo772")
                ],
            ]
        )
    )


@app.on_message(command(["‹ متحركه ›", "متحركه"]) & filters.private)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id,url,caption="↯ : تم اختيار المتحركه اليك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/terbo772")
                ],
            ]
        )
    )

@app.on_message(command(["‹ اقتباسات ›", "اقتباسات"]) & filters.private)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯ : تم اختيار اقتباس اليك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/terbo772")
                ],
            ]
        )
    )

@app.on_message(command(["هيدرات", "‹ هيدرات ›"]) & filters.private)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/flflfldld/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯ : تم اختيار هيدرات اليك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/terbo772")
                ],
            ]
        )
    )

@app.on_message(command(["‹ افتارات شباب ›"]) & filters.private)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/QrQsQ/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯ : تم اختيار صوره اليك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/terbo772")
                ],
            ]
        )
    )

@app.on_message(command(["‹ افتار بنات ›"]) & filters.private)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯ : تم اختيار صوره اليك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/terbo772")
                ],
            ]
        )
    )


@app.on_message(command(["‹ قران ›", "قران"]) & filters.private)
async def ihd(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/lllIIlIllIlIIlI/{rl}"
    await client.send_voice(message.chat.id,url,caption="↯ : تم اختيار ايـه قرآنيه اليك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/terbo772")
                ],
            ]
        )
    )

