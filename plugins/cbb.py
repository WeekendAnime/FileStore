#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Sєиραι : <a href='tg://user?id={OWNER_ID}'>Jҽϝϝɾҽყ ʂαɱα</a>\n○ Aиιмє ωєєкєи∂ѕ : <a href='https://t.me/Anime_Weekends'>Cℓιcк нєяє</a>\n○ Oиgσιиg ωєєкєи∂ѕ : <a href='https://t.me/Ongoing_Weekends'>Cℓιcк нєяє</a>\n○ Mσνιє ωєєкєи∂ѕ : <a href='https://t.me/movie_dist'>Cℓιcк нєяє</a>\n○ Wєєкєи∂ѕ ωєєвѕ : <a href='https://t.me/Weebs_Weekends'>Cℓιcк нєяє</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ', url='https://t.me/Anime_Weekends')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
