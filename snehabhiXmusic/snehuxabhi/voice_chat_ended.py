from pyrogram import Client, filters

from pyrogram.types import Message

from snehabhiXmusic.abhi.channelmusic import get_chat_id

from snehabhiXmusic.services.callsmusic import remove

@Client.on_message(filters.voice_chat_ended)

async def voice_chat_ended(_, message: Message):

    try:

        remove(get_chat_id(message.chat))

    except Exception:

        pass
