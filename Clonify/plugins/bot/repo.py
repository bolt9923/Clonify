from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Clonify import app
from config import BOT_USERNAME
from Clonify.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**Cʟᴏɴɪғʏ** - Tʜᴇ Uʟᴛɪᴍᴀᴛᴇ Tᴇʟᴇɢʀᴀᴍ Mᴜsɪᴄ Sᴏʟᴜᴛɪᴏɴ ᴡɪᴛʜ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇs.

┏━━━━━━━━━━━━━━━━━⧫
┠ ◆ **sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ:** [Click Here](https://t.me/NlTRIDE)  
┠ ◆ **ᴅᴇᴠᴇʟᴏᴘᴇʀ:** [ᴛᴇᴀᴍ ʜᴜɴᴛᴇʀs](https://t.me/huntermafiya)
┠ ◆ **ʀᴇʟᴇᴀsᴇᴅ ʙʏ:** [ʀᴀʀᴇ ʙᴏᴛs](https://t.me/huntermafiya)
┗━━━━━━━━━━━━━━━━━⧫

__Fᴏʀᴋ ɪᴛ, ᴄᴜsᴛᴏᴍɪᴢᴇ ɪᴛ, ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ʏᴏᴜʀ ᴏᴡɴ!__
"""





@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
                InlineKeyboardButton("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/huntermafiya"),
                InlineKeyboardButton("𝗨𝗣𝗗𝗔𝗧𝗘", url="https://t.me/NLTRIDE")
        ],
        [ 
          InlineKeyboardButton("𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘", url=f"https://t.me/NLTRIDE")
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/axv2m3.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://t.me/NLTRIDE")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://t.me/NLTRIDE) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/huntermafiya)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
