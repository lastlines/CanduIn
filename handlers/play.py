import os
from os import path
from typing import Dict
from pyrogram import Client, filters, emoji
from pyrogram.types import Message, Voice, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.errors.exceptions.flood_420 import FloodWait
from typing import Callable, Coroutine, Dict, List, Tuple, Union
from pyrogram.errors import UserAlreadyParticipant
from callsmusic import callsmusic, queues
from callsmusic.callsmusic import client as USER
from helpers.admins import get_administrators
import requests
import aiohttp
import youtube_dl
from youtube_search import YoutubeSearch
import converter
from downloaders import youtube
from config import DURATION_LIMIT
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only
from helpers.errors import DurationLimitError
from helpers.gets import get_url, get_file_name
import aiofiles
import ffmpeg
from PIL import Image, ImageFont, ImageDraw
from config import que
from cache.admins import admins as a
import traceback
import sys
import json
import wget
chat_id = None


def transcode(filename):
    ffmpeg.input(filename).output("input.raw", format='s16le', acodec='pcm_s16le', ac=2, ar='48k').overwrite_output().run() 
    os.remove(filename)

# Convert seconds to mm:ss
def convert_seconds(seconds):
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)


# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


# Change image size
def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image1 = Image.open("./background.png")
    image2 = Image.open("etc/foreground.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save("temp.png")
    img = Image.open("temp.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("etc/font.otf", 32)
    draw.text((190, 550), f"Judul : {title}", (255, 255, 255), font=font)
    draw.text(
        (190, 590), f"Durasi : {duration}", (255, 255, 255), font=font
    )
    draw.text((190, 630), f"Views : {views}", (255, 255, 255), font=font)
    draw.text((190, 670),
        f"Request By: {requested_by}",
        (255, 255, 255),
        font=font,
    )
    img.save("final.png")
    os.remove("temp.png")
    os.remove("background.png")

@Client.on_message(
    filters.command("playlist")
    & filters.group
    & ~ filters.edited
)
async def playlist(client, message):
    global que
    queue = que.get(message.chat.id)
    if not queue:
        await message.reply_text('❌ Tidak Ada Playlist')
    temp = []
    for t in queue:
        temp.append(t)
    now_playing = temp[0][0]
    by = temp[0][1].mention(style='md')
    msg = "**Lagu Yang Sedang Diputar** di {}".format(message.chat.title)
    msg += "\n\nJudul : "+ now_playing
    msg += "\nRequest Dari : "+by
    temp.pop(0)
    if temp:
        msg += '\n───────────────────────────'
        msg += '\n**Antrian Lagu :**'
        for song in temp:
            name = song[0]
            usr = song[1].mention(style='md')
            msg += f'\n\nJudul : {name}'
            msg += f'\nRequest Dari : {usr}\n'
    await message.reply_text(msg)    
    

@Client.on_message(
    filters.command("current")
    & filters.group
    & ~ filters.edited
)
async def ee(client, message):
    queue = que.get(message.chat.id)
    stats = updated_stats(message.chat, queue)
    if stats:
        await message.reply(stats)              
    else:
        await message.reply('Tidak Ada Music')    
    



@Client.on_message(command("play") 
                   & filters.group
                   & ~filters.edited 
                   & ~filters.forwarded
                   & ~filters.via_bot)
async def play(_, message: Message):

    lel = await message.reply("🔄 **Tunggu...**")
    
    administrators = await get_administrators(message.chat)
    chid = message.chat.id

    try:
        user = await USER.get_me()
    except:
        user.first_name = "CanduIn"
    usar = user
    wew = usar.id
    try:
        await _.get_chat_member(chid, wew)
    except:
        for administrator in administrators:
            if administrator == message.from_user.id:
                try:
                    invitelink = await _.export_chat_invite_link(chid)
                except:
                    await lel.edit(
                        "<b>⚠️ Jadikan Bot sebagai Admin dulu!</b>")
                    return

                try:
                    await USER.join_chat(invitelink)
                    await USER.send_message(
                        message.chat.id, "**𝐂𝐚𝐧𝐝𝐮𝐌𝐮𝐬𝐢𝐜 Assisten berhasil bergabung dengan Group anda 🎵**")

                except UserAlreadyParticipant:
                    pass
                except Exception:
                    await lel.edit(
                        f"<b>🛑 Flood Wait Error 🛑</b> \n\Hey {user.first_name} tidak dapat bergabung dengan grup Anda karena banyaknya permintaan bergabung! Pastikan pengguna tidak dibanned dalam grup. dan Coba Lagi!")
    try:
        await USER.get_chat(chid)
    except:
        await lel.edit(
            f"<i>Hey {user.first_name}  terkena banned dari Grup ini, Minta admin untuk mengirim perintah `/play` untuk pertama kalinya atau tambahkan @robotassistenv2 secara manual</i>")
        return
    
    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"❌ **Lagu dengan durasi lebih dari** {DURATION_LIMIT} **menit. Tidak Diizinkan!**"
            )

        file_name = get_file_name(audio)
        title = file_name
        thumb_name = "https://telegra.ph/file/41126266cb7db2240e798.png"
        thumbnail = thumb_name
        duration = round(audio.duration / 60)
        views = "Locally added"

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("☕ ᴜᴘᴅᴀᴛᴇ", url="https://t.me/robotprojectx"),
                    InlineKeyboardButton("ᴏᴡɴᴇʀ ☕", url="https://t.me/justthetech"),
                ],
                [InlineKeyboardButton(text="❌", callback_data="cls")],
            ]
        )
        
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)  
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )

    elif url:
        try:
            results = YoutubeSearch(url, max_results=1).to_dict()
            # print results
            title = results[0]["title"]       
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f'thumb{title}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")
            
            secmul, dur, dur_arr = 1, 0, duration.split(':')
            for i in range(len(dur_arr)-1, -1, -1):
                dur += (int(dur_arr[i]) * secmul)
                secmul *= 60
                
            keyboard = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("☕ ᴜᴘᴅᴀᴛᴇ", url="https://t.me/robotprojectx"),
                    InlineKeyboardButton("ᴏᴡɴᴇʀ ☕", url="https://t.me/justthetech"),
                    ],
                    [InlineKeyboardButton(text="❌", callback_data="cls")],
                ]   
            )
        except Exception as e:
            title = "NaN"
            thumb_name = "https://telegra.ph/file/41126266cb7db2240e798.png"
            duration = "NaN"
            views = "NaN"
            keyboard = InlineKeyboardMarkup(
                    [
                        [
                        InlineKeyboardButton("☕ ᴜᴘᴅᴀᴛᴇ", url="https://t.me/robotprojectx"),
                        InlineKeyboardButton("ᴏᴡɴᴇʀ ☕", url="https://t.me/justthetech"),
                        ],
                        [InlineKeyboardButton(text="❌", callback_data="cls")],
                    ]       
                )
        if (dur / 60) > DURATION_LIMIT:
             await lel.edit(f"❌ **Lagu dengan durasi lebih dari** {DURATION_LIMIT} **menit. Tidak Diizinkan!**")
             return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)     
        file_path = await converter.convert(youtube.download(url))
    else:
        if len(message.command) < 2:
            return await lel.edit("❁ <b>Music</b> tidak ditemukan.\n❁ Ketik /play (judul lagu).\n❁ Ketik /search (judul lagu).")
        await lel.edit("🔎 **Mencari...**")
        query = message.text.split(None, 1)[1]
        # print(query)
        await lel.edit("🎵 **Music Sedang Diproses...**")
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            url = f"https://youtube.com{results[0]['url_suffix']}"
            # print results
            title = results[0]["title"]       
            thumbnail = results[0]["thumbnails"][0]
            thumb_name = f'thumb{title}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)
            duration = results[0]["duration"]
            url_suffix = results[0]["url_suffix"]
            views = results[0]["views"]
            durl = url
            durl = durl.replace("youtube", "youtubepp")

            secmul, dur, dur_arr = 1, 0, duration.split(':')
            for i in range(len(dur_arr)-1, -1, -1):
                dur += (int(dur_arr[i]) * secmul)
                secmul *= 60
                
        except Exception as e:
            await lel.edit(
                "❁ <b>Music</b> tidak ditemukan.\n❁ Ketik /play (judul lagu).\n❁ Ketik /search (judul lagu)."
            )
            print(str(e))
            return

        keyboard = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("☕ ᴜᴘᴅᴀᴛᴇ", url="https://t.me/robotprojectx"),
                    InlineKeyboardButton("ᴏᴡɴᴇʀ ☕", url="https://t.me/justthetech"),
                    ],
                    [InlineKeyboardButton(text="❌", callback_data="cls")],
                ]   
            )
        
        if (dur / 60) > DURATION_LIMIT:
             await lel.edit(f"❌ **Lagu dengan durasi lebih dari** {DURATION_LIMIT} **menit. Tidak Diizinkan!**")
             return
        requested_by = message.from_user.first_name
        await generate_cover(requested_by, title, views, duration, thumbnail)  
        file_path = await converter.convert(youtube.download(url))
  
    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        qeue = que.get(message.chat.id)
        s_name = title
        r_by = message.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]
        qeue.append(appendable)
        await message.reply_photo(
        photo="final.png", 
        caption=f"☕ **Judul** : [{title}]({url}) \n#️⃣ **Antrian** : {position}",
        reply_markup=keyboard)
        os.remove("final.png")
        return await lel.delete()
    else:
        chat_id = message.chat.id
        que[chat_id] = []
        qeue = que.get(message.chat.id)
        s_name = title            
        r_by = message.from_user
        loc = file_path
        appendable = [s_name, r_by, loc]      
        qeue.append(appendable)
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo="final.png",
        reply_markup=keyboard,
        caption=f"📋 **Judul :** [{title[:60]}]({url})\n⏱️ **Durasi :** {duration}\n" \
                    + f"👤 **Request Dari :** {message.from_user.mention}",
        )
    
        os.remove("final.png")
        return await lel.delete() 
