import os
from os import getenv
from dotenv import load_dotenv


if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "SNEHABHI OP BOTZ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/bc6ecaac6eb57cb10342c.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/5c1bd95f066aad81df745.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/bc6ecaac6eb57cb10342c.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/bc6ecaac6eb57cb10342c.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/bc6ecaac6eb57cb10342c.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/5c1bd95f066aad81df745.png")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "SNEHABHI_BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SNEHABHI_MUSICS")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "SNEHABHI_SERVER")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "SNEHABHI_UPDATES")
# isi dengan username kamu tanpa simbol @
OWNER_NAME = getenv("OWNER_NAME", "ABHI_IZ_MINE")
# fill with your nickname
ALIVE_NAME = getenv("ALIVE_NAME", "SNEHABHI OP BOTZ")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID"))
DATABASE_URL = os.environ.get("DATABASE_URL")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . x *").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/SNEHABHIxd/SNEHU-MUSIC"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
