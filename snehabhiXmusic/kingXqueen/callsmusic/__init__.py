from pyrogram import Client
from snehabhiXmusic.kingXqueen.callsmusic import pytgcalls, run
from snehabhiXmusic import config

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)

run = client.run
