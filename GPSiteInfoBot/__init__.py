import logging
import os
import sys
import time
import threading
import telegram.ext as tg

from telegram.ext import CallbackContext
from telethon import TelegramClient

StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.")
    quit(1)


try:
    API_ID = 2076846
    API_HASH = "a7c38b63155953f8c529718a3ac0003a"
    CERT_PATH = os.environ.get("CERT_PATH")
    DB_URI = os.environ.get("DATABASE_URL")
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
    INFOPIC = bool(os.environ.get("INFOPIC", False))
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    PORT = int(os.environ.get("PORT", 5000))
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
    URL = os.environ.get("URL", "")  # Does not contain token
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
except
    pass



telethn = TelegramClient("TelethonBot", API_ID, API_HASH)
updater = tg.Updater(TOKEN, workers=8, use_context=True)
bot = updater.bot
dispatcher = updater.dispatcher

SUDO_USERS.add(OWNER_ID)


AUTHORIZED_CHATS = list(AUTHORIZED_CHATS)
SUDO_USERS = list(SUDO_USERS)

# Load at end to ensure all prev variables have been set
from GPSiteInfoBot.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler)

# make sure the regex handler can take extra kwargs
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
