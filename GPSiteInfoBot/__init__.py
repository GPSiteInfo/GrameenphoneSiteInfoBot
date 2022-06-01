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
    BOT_TOKEN = "5022788742:AAEk4DvdxA1mfBbPFs8xvB65rbJJq1YKBlE"
    CERT_PATH = os.environ.get("CERT_PATH")
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
    INFOPIC = bool(os.environ.get("INFOPIC", False))
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    OWNER_ID = os.environ.get("OWNER_ID", None)
    PORT = int(os.environ.get("PORT", 5000))
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
    URL = os.environ.get("URL", "")  # Does not contain token
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
except KeyError as e:
    LOGGER.error("One or more environment variables missing!")
    exit(1)


telethn = TelegramClient("TelethonBot", API_ID, API_HASH)
updater = tg.Updater(BOT_TOKEN, workers=8, use_context=True)
bot = updater.bot
dispatcher = updater.dispatcher
