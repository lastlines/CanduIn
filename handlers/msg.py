# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

class Messages():
      START_MSG = "🎶 **Hello Friends**, [{}](tg://user?id={}) 👏\nSaya 𝐂𝐚𝐧𝐝𝐮𝐌𝐮𝐬𝐢𝐜𝐁𝐨𝐭, Saya akan membantumu **memutar music** di Voice Chat Telegram Groups & Channel, dengan **fitur-fitur** yang menarik.\n\n❗Ketik /help untuk melihat **panduan pemakaiannya**.\n❗Ketik /start untuk **memuat ulang**.\n\n───────────────────────────────────\n\n𝑺𝒆𝒎𝒖𝒂 𝒐𝒓𝒂𝒏𝒈 𝒑𝒂𝒔𝒕𝒊 𝒎𝒂𝒕𝒊, 𝒕𝒂𝒑𝒊 𝒕𝒊𝒅𝒂𝒌 𝒔𝒆𝒎𝒖𝒂 𝒐𝒓𝒂𝒏𝒈 𝒅𝒂𝒑𝒂𝒕 𝒎𝒆𝒎𝒃𝒆𝒓𝒊 𝒂𝒓𝒕𝒊. 𝑷𝒂𝒔𝒕𝒊𝒌𝒂𝒏 𝒉𝒊𝒅𝒖𝒑𝒎𝒖 𝒃𝒆𝒓𝒂𝒓𝒕𝒊/𝒃𝒆𝒓𝒎𝒂𝒏𝒇𝒂𝒂𝒕 𝒖𝒏𝒕𝒖𝒌 𝒐𝒓𝒂𝒏𝒈 𝒍𝒂𝒊𝒏\n\n───────────────────────────────────\n\n❃ **Manage by :  [°ᴹᴿ° | ℝ𝕆𝔹𝕆𝕋](https://t.me/justthetech)  ☕\n❃ Support dengan doa aja guys! Thanks!\n❃ NB : Maaf jika ada kekurangan didalam bot ini**"

      HELP_MSG = [
        ".",
f"""
**Hello Friends, Saya adalah 𝐂𝐚𝐧𝐝𝐮𝐌𝐮𝐬𝐢𝐜𝐁𝐨𝐭
\n❂ 𝙈𝙖𝙨𝙪𝙠𝙠𝙖𝙣 𝘽𝙤𝙩 >> @candumusic_bot 
❂ 𝙈𝙖𝙨𝙪𝙠𝙠𝙖𝙣 𝘼𝙨𝙨𝙞𝙨𝙩𝙚𝙣 >> @robotassistenv2**

𝙎𝙚𝙩𝙩𝙞𝙣𝙜 𝘽𝙤𝙩 :

𝟏) 𝑱𝒂𝒅𝒊𝒌𝒂𝒏 𝒃𝒐𝒕 𝒔𝒆𝒃𝒂𝒈𝒂𝒊 **𝑨𝒅𝒎𝒊𝒏** 
𝟐) 𝑺𝒕𝒂𝒓𝒕 𝒗𝒐𝒊𝒄𝒆 𝒄𝒉𝒂𝒕 
𝟑) 𝑲𝒆𝒕𝒊𝒌 /play [𝒋𝒖𝒅𝒖𝒍 𝒍𝒂𝒈𝒖]  
*) 𝑷𝒂𝒔𝒕𝒊𝒌𝒂𝒏 𝒔𝒖𝒅𝒂𝒉 𝒎𝒆𝒎𝒂𝒔𝒖𝒌𝒌𝒂𝒏 𝒂𝒔𝒔𝒊𝒔𝒕𝒆𝒏 >> @robotassistenv2 𝒅𝒊𝒅𝒂𝒍𝒂𝒎 𝑮𝒓𝒖𝒃. 
""", 

f""" 
𝘽𝙚𝙧𝙞𝙠𝙪𝙩 𝘿𝙖𝙛𝙩𝙖𝙧 𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 𝙮𝙖𝙣𝙜 𝙙𝙖𝙥𝙖𝙩 𝙙𝙞𝙜𝙪𝙣𝙖𝙠𝙖𝙣 :
╔═════════════════════════════════
╠═ /play: 𝘗𝘭𝘢𝘺 𝘮𝘶𝘴𝘪𝘤 𝘥𝘢𝘳𝘪 𝘺𝘰𝘶𝘵𝘶𝘣𝘦 𝘱𝘦𝘯𝘤𝘢𝘳𝘪𝘢𝘯 𝘱𝘦𝘳𝘵𝘢𝘮𝘢 
╠═ /play [yt link] : 𝘗𝘭𝘢𝘺 𝘮𝘶𝘴𝘪𝘤 𝘥𝘢𝘳𝘪 𝘭𝘪𝘯𝘬 𝘺𝘰𝘶𝘵𝘶𝘣𝘦 
╠═ /play [reply ke audio]: 𝘗𝘭𝘢𝘺 𝘮𝘶𝘴𝘪𝘤 𝘥𝘢𝘳𝘪 𝘧𝘪𝘭𝘦
╠═ /song [judul lagu] : 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘭𝘢𝘨𝘶
╠═════════════════════════════════
╠═ /skip : 𝘚𝘬𝘪𝘱 𝘬𝘦 𝘮𝘶𝘴𝘪𝘤 𝘣𝘦𝘳𝘪𝘬𝘶𝘵𝘯𝘺𝘢
╠═ /pause : 𝘔𝘦𝘯𝘨𝘩𝘦𝘯𝘵𝘪𝘬𝘢𝘯 𝘮𝘶𝘴𝘪𝘤 𝘴𝘦𝘮𝘦𝘯𝘵𝘢𝘳𝘢
╠═ /resume : 𝘔𝘦𝘭𝘢𝘯𝘫𝘶𝘵𝘬𝘢𝘯 𝘮𝘶𝘴𝘪𝘤
╠═ /end : 𝘔𝘦𝘯𝘨𝘩𝘦𝘯𝘵𝘪𝘬𝘢𝘯 𝘮𝘶𝘴𝘪𝘤
╠═ /current : 𝘔𝘦𝘭𝘪𝘩𝘢𝘵 𝘮𝘶𝘴𝘪𝘤 𝘺𝘢𝘯𝘨 𝘴𝘦𝘥𝘢𝘯𝘨 𝘥𝘪𝘮𝘢𝘪𝘯𝘬𝘢𝘯
╠═ /playlist : 𝘔𝘦𝘭𝘪𝘩𝘢𝘵 𝘥𝘢𝘧𝘵𝘢𝘳 𝘢𝘯𝘵𝘳𝘪𝘢𝘯
╠═════════════════════════════════
╠═ /admincache : 𝘙𝘦𝘧𝘳𝘦𝘴𝘩 𝘈𝘥𝘮𝘪𝘯 𝘎𝘳𝘶𝘣
╠═ /userbotjoin : 𝘐𝘯𝘷𝘪𝘵𝘦 𝘈𝘴𝘴𝘪𝘴𝘵𝘦𝘯 𝘖𝘵𝘰𝘮𝘢𝘵𝘪𝘴
╠═ /reload : 𝘙𝘦𝘭𝘰𝘢𝘥 𝘈𝘥𝘮𝘪𝘯 𝘎𝘳𝘶𝘣
╚═════════════════════════════════
""", 

f""" 🎶 **Hello Friends**, Saya 𝐂𝐚𝐧𝐝𝐮𝐌𝐮𝐬𝐢𝐜𝐁𝐨𝐭! 👏
Saya akan membantumu **memutar music** di Telegram Groups & Channel, dengan **fitur-fitur** yang menarik.
\n❗ Ketik /help untuk **panduan pemakaiannya**.
❗ Ketik /start untuk **memuat ulang**.
\n───────────────────────────────────
\n𝑺𝒆𝒎𝒖𝒂 𝒐𝒓𝒂𝒏𝒈 𝒑𝒂𝒔𝒕𝒊 𝒎𝒂𝒕𝒊, 𝒕𝒂𝒑𝒊 𝒕𝒊𝒅𝒂𝒌 𝒔𝒆𝒎𝒖𝒂 𝒐𝒓𝒂𝒏𝒈 𝒅𝒂𝒑𝒂𝒕 𝒎𝒆𝒎𝒃𝒆𝒓𝒊 𝒂𝒓𝒕𝒊. 𝑷𝒂𝒔𝒕𝒊𝒌𝒂𝒏 𝒉𝒊𝒅𝒖𝒑𝒎𝒖 𝒃𝒆𝒓𝒂𝒓𝒕𝒊/𝒃𝒆𝒓𝒎𝒂𝒏𝒇𝒂𝒂𝒕 𝒖𝒏𝒕𝒖𝒌 𝒐𝒓𝒂𝒏𝒈 𝒍𝒂𝒊𝒏
\n───────────────────────────────────
\n❃ **Manage by :  [°ᴹᴿ° | ℝ𝕆𝔹𝕆𝕋](https://t.me/justthetech)
❃ Support dengan doa aja guys! Thanks!
❃ NB : Maaf jika ada kekurangan didalam bot ini**
"""
      ]
