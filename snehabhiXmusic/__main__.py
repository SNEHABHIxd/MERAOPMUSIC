import requests

from pyrogram import Client as Bot

from snehabhiXmusic.config import API_HASH, API_ID, BG_IMAGE, BOT_TOKEN

from Client.callsmusic import run

response = requests.get(BG_IMAGE)

file = open("./etc/snehuxabhi.jpg", "wb")

file.write(response.content)

file.close()

bot = Bot(

    ":memory:",

    API_ID,

    API_HASH,

    bot_token=BOT_TOKEN,

    plugins=dict(root="snehabhiXmusic.snehuxabhi"),

)

bot.start()

run()
