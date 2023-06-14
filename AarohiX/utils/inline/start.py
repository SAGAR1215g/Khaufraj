from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ [❤‍🔥ᴅɪʟ❤‍🔥] 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣️ʜᴇʟᴩ❣️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥sᴇᴛᴛɪɴɢs❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥰 ғᴇᴇʟɪɴɢs 🥰", url=f"https://t.me/dil_ki_duniya"),
            InlineKeyboardButton(
                text="🥰 ᴋʜᴀᴜғ[❣️] 🥰", url=f"https://II_KHAUF_X_II"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥰ᴅɪʟ[❣️]🥰", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ[ᴀɪᴍ]🥰", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ [💞ᴅɪʟ💞]🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥺ʜᴇʟᴩ & ᴍᴇɴᴛɪᴏɴ ᴄᴏᴍᴍᴀɴᴅ🥺", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥰 ғᴇᴇʟɪɴɢs 🥰", url=f"https://t.me/dil_ki_duniya"),
            InlineKeyboardButton(
                text="🥰 ᴍʏ ʟɪғᴇʟɪɴᴇ[❣️] 🥰", url=f"https://t.me/Dil_ki_Ishu"
            ),
        ],
        [
            InlineKeyboardButton(text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ[ᴅɪʟ]💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰sᴜᴩᴩᴏʀᴛ[ᴀɪᴍ]🥰", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🥰 ᴏᴡɴᴇʀ 🥰", url=f"https://t.me/Dil_ki_Ishu"
                ),
        ],
     ]
    return buttons
