# +++ Made By King [telegram username: @Shidoteshika1] +++

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from bot import Bot
from helper_func import encode, get_message_id, is_admin

async def cancelkeyMarkup(message: Message, text:str):
    await message.reply(
        text=text,
        disable_web_page_preview=True,
        reply_markup=ReplyKeyboardMarkup(
            [['CANCEL']], 
            one_time_keyboard=True, 
            resize_keyboard=True
        )
    )

async def verify_cancel(message:Message):
    text_msg = message.text

    if text_msg and text_msg == "CANCEL":
        await message.reply("❌ Cᴀɴᴄᴇʟʟᴇᴅ...")
        await message.delete()
        return True
    
    return False


@Bot.on_message(filters.command('batch') & filters.private & is_admin)
async def batch(client: Client, message: Message):
    channel = f"<a href={client.db_channel.invite_link}>ᴅʙ ᴄʜᴀɴɴᴇʟ</a>" 
    while True:
        try:
            await cancelkeyMarkup(
                message, 
                text=f"<b><blockquote>Fᴏʀᴡᴀʀᴅ ᴛʜᴇ Fɪʀsᴛ Mᴇssᴀɢᴇ ғʀᴏᴍ {channel} (ᴡɪᴛʜ ǫᴜᴏᴛᴇs)..</blockquote>\n<blockquote>Oʀ Sᴇɴᴅ ᴛʜᴇ {channel} Pᴏsᴛ Lɪɴᴋ</blockquote></b>"
            )
            
            first_message = await client.listen(chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)))

        except:
            return
        
        if await verify_cancel(first_message):
            return

        f_msg_id = await get_message_id(client, first_message)

        if f_msg_id:
            break
        else:
            await first_message.reply(f"<b>❌ Eʀʀᴏʀ..\n<blockquote>Tʜɪs Fᴏʀᴡᴀʀᴅᴇᴅ ᴘᴏsᴛ ᴏʀ ᴍᴇssᴀɢᴇ ʟɪɴᴋ ɪs ɴᴏᴛ ғʀᴏᴍ ᴍʏ {channel}</blockquote></b>", quote = True, disable_web_page_preview=True)
            continue

    while True:
        try:
            await cancelkeyMarkup(
                message, 
                text=f"<b><blockquote>Fᴏʀᴡᴀʀᴅ ᴛʜᴇ Lᴀsᴛ Mᴇssᴀɢᴇ ғʀᴏᴍ {channel} (ᴡɪᴛʜ ǫᴜᴏᴛᴇs)..</blockquote>\n<blockquote>Oʀ Sᴇɴᴅ ᴛʜᴇ {channel} Pᴏsᴛ Lɪɴᴋ</blockquote></b>"
            )
            
            second_message = await client.listen(chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)))
        except:
            return
        
        if await verify_cancel(second_message):
            return
        
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply(f"<b>❌ Eʀʀᴏʀ..\n<blockquote>Tʜɪs Fᴏʀᴡᴀʀᴅᴇᴅ ᴘᴏsᴛ ᴏʀ ᴍᴇssᴀɢᴇ ʟɪɴᴋ ɪs ɴᴏᴛ ғʀᴏᴍ ᴍʏ {channel}</blockquote></b>", quote=True, reply_markup=reply_markup, disable_web_page_preview=True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Sʜᴀʀᴇ URL", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>Bᴇʟᴏᴡ ɪs ʏᴏᴜʀ ʟɪɴᴋ:</b>\n<blockquote>{link}</blockquote>", quote=True, reply_markup=reply_markup, disable_web_page_preview=True)


@Bot.on_message(filters.command('genlink') & filters.private & is_admin)
async def link_generator(client: Client, message: Message):
    channel = f"<a href={client.db_channel.invite_link}>ᴅʙ ᴄʜᴀɴɴᴇʟ</a>"
    while True:
        try:
            await cancelkeyMarkup(
                message, 
                text=f"<b><blockquote>Fᴏʀᴡᴀʀᴅ ᴛʜᴇ Mᴇssᴀɢᴇ ғʀᴏᴍ {channel} (ᴡɪᴛʜ ǫᴜᴏᴛᴇs)..</blockquote>\n<blockquote>Oʀ Sᴇɴᴅ ᴛʜᴇ {channel} Pᴏsᴛ Lɪɴᴋ</blockquote></b>"
            )
            
            channel_message = await client.listen(chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)))
        except:
            return
        
        if await verify_cancel(channel_message):
            return
        
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply(f"<b>❌ Eʀʀᴏʀ..\n<blockquote>Tʜɪs Fᴏʀᴡᴀʀᴅᴇᴅ ᴘᴏsᴛ ᴏʀ ᴍᴇssᴀɢᴇ ʟɪɴᴋ ɪs ɴᴏᴛ ғʀᴏᴍ ᴍʏ {channel}</blockquote></b>", quote=True, disable_web_page_preview=True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Sʜᴀʀᴇ URL", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>Bᴇʟᴏᴡ ɪs ʏᴏᴜʀ ʟɪɴᴋ:</b>\n<blockquote>{link}</blockquote>", quote=True, reply_markup=reply_markup, disable_web_page_preview=True)
