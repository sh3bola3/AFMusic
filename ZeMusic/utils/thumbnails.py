import asyncio
import os
import random
import re
import textwrap
import aiofiles
import aiohttp
from ZeMusic import app

from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch
import numpy as np
from config import YOUTUBE_IMG_URL
A = "De"
B = "v : @"
D = "IC"
E = "_"
V = "19"
DEV = A+B+D+E+V
def make_col():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

def truncate(text):
    list = text.split(" ")
    text1 = ""
    text2 = ""
    for i in list:
        if len(text1) + len(i) < 30:
            text1 += " " + i
        elif len(text2) + len(i) < 30:
            text2 += " " + i
    text1 = text1.strip()
    text2 = text2.strip()
    return [text1, text2]

async def get_thumb(videoid):
    try:
        if os.path.isfile(f"cache/{videoid}.jpg"):
            return f"cache/{videoid}.jpg"
        url = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(f"http://img.youtube.com/vi/{videoid}/maxresdefault.jpg") as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"cache/thumb{videoid}.jpg", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"cache/thumb{videoid}.jpg")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(30))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        image2 = background

        # Create circular thumbnail
        lum_img = Image.new("L", [720, 720], 0)
        draw = ImageDraw.Draw(lum_img)
        draw.pieslice([(0, 0), (720, 720)], 0, 360, fill=255, outline="white")
        img_arr = np.array(image1.crop((280, 0, 1000, 720)))
        lum_img_arr = np.array(lum_img)
        final_img_arr = np.dstack((img_arr, lum_img_arr))
        circular_thumb = Image.fromarray(final_img_arr).resize((600, 600))

        image2.paste(circular_thumb, (50, 70), mask=circular_thumb)

        # fonts
        font1 = ImageFont.truetype("ZeMusic/assets/font.ttf", 30)
        font2 = ImageFont.truetype("ZeMusic/assets/font2.ttf", 70)
        font3 = ImageFont.truetype("ZeMusic/assets/font2.ttf", 40)
        font4 = ImageFont.truetype("ZeMusic/assets/font2.ttf", 35)

        image4 = ImageDraw.Draw(image2)
        image4.text((20, 10), f" {DEV}", fill="white", font=font1, align="left")
        image4.text((680, 150), "TERBO MUSIC", fill="white", font=font2, stroke_width=2, stroke_fill="white", align="left")

        # title
        title1 = truncate(title)
        image4.text((680, 300), text=title1[0], fill="white", stroke_width=1, stroke_fill="white", font=font3, align="left")
        image4.text((680, 350), text=title1[1], fill="white", stroke_width=1, stroke_fill="white", font=font3, align="left")

        # description
        views_text = f"Views : {views}"
        duration_text = f"Duration : {duration} Mins"
        channel_text = f"Channel : @EF_19"

        image4.text((680, 450), text=views_text, fill="white", font=font4, align="left")
        image4.text((680, 500), text=duration_text, fill="white", font=font4, align="left")
        image4.text((680, 550), text=channel_text, fill="white", font=font4, align="left")

        image2 = ImageOps.expand(image2, border=10, fill=make_col())
        image2 = image2.convert("RGB")
        image2.save(f"cache/{videoid}.jpg")
        file = f"cache/{videoid}.jpg"
        return file
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL
