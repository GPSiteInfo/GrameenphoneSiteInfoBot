import importlib
import time
import re
from sys import argv
from typing import Optional

from GPSiteInfoBot import (
    CERT_PATH,
    LOGGER,
    OWNER_ID,
    PORT,
    BOT_TOKEN,
    URL,
    WEBHOOK,
    dispatcher,
    StartTime,
    SUPPORT_CHAT,
    telethn,
    updater)

# needed to dynamically load modules
# NOTE: Module order is not guaranteed, specify that in the config file!
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from telegram.error import (BadRequest, ChatMigrated, NetworkError, TelegramError, TimedOut, Unauthorized)

from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler)


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


PM_START_TEXT = """
Hello {}, I'm {}. [ ](https://telegra.ph/file/b9b8713a3376bea56e6b6.jpg)
I am a group management bot.
I can manage your group with lots of useful features.
For commands and help press /help .
"""


HELP_TEXT = """
Hey there! My name is *{}*.
I'm a Hero For Fun and help admins manage their groups. Have a look at the following for an idea of some of \
the things I can help you with.

*Main* commands available:
 • /help: PM's you this message.
 • /help <module name>: PM's you info about that module.
 • /settings:
   • in PM: will send you your settings for all supported modules.
   • in a group: will redirect you to pm, with all that chat's settings.

{}
And the following:
""".format(
    dispatcher.bot.first_name,
    "All commands can either be used with /")


IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}
GDPR = []


dispatcher.run_async
def start(update: Update, context: CallbackContext):
    args = context.args
    uptime = get_readable_time((time.time() - StartTime))
    if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                send_help(update.effective_chat.id, HELP_TEXT)
            elif args[0].lower().startswith("ghelp_"):
                mod = args[0].lower().split("_", 1)[1]
                if not HELPABLE.get(mod, False):
                    return
                send_help(
                    update.effective_chat.id,
                    HELPABLE[mod].__help__,
                    InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="Back", callback_data="help_back")]]))
            elif args[0].lower() == "markdownhelp":
                IMPORTED["extras"].markdown_help_sender(update)
            elif args[0].lower() == "disasters":
                IMPORTED["disasters"].send_disasters(update)
            elif args[0].lower().startswith("stngs_"):
                match = re.match("stngs_(.*)", args[0].lower())
                chat = dispatcher.bot.getChat(match.group(1))

                if is_user_admin(chat, update.effective_user.id):
                    send_settings(match.group(1), update.effective_user.id, False)
                else:
                    send_settings(match.group(1), update.effective_user.id, True)

            elif args[0][1:].isdigit() and "rules" in IMPORTED:
                IMPORTED["rules"].send_rules(update, args[0], from_pm=True)

        else:
            first_name = update.effective_user.first_name
            last_name = update.effective_user.last_name
            update.effective_message.reply_text(
                PM_START_TEXT.format(
                    escape_markdown(first_name), escape_markdown(context.bot.first_name)),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            text="✅ Add Opimus Prime in your group",
                            url="t.me/{}?startgroup=true".format(
                                context.bot.username))
                    ],
                     [
                         InlineKeyboardButton(
                             text="🚨 Support Group",
                             url=f"https://t.me/{SUPPORT_CHAT}"),
                         InlineKeyboardButton(
                             text="♂ Commands",
                             callback_data="help_back")
                    ], 
                     [
                         InlineKeyboardButton(
                             text="📥 Mirror Bot Group ",
                             url="https://t.me/+WKZqyWNHpLViMmI1"),
                         InlineKeyboardButton(
                             text="🔁 Repository",
                             url="https://github.com/Al-Noman-Pro/GPSiteInfoBot")
                    ]]))
    else:           
        update.effective_message.reply_text(
            GROUP_START_TEXT,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(GROUP_START_BUTTONS))


GROUP_START_TEXT = """
Hi ,I am Optimus Prime Bot.
I'm a group management bot.
"""

GROUP_START_BUTTONS = [[InlineKeyboardButton(text="☸ Repository", url="https://github.com/Al-Noman-Pro/GPSiteInfoBot")],

                      [InlineKeyboardButton(text="✅ Add me in your group", url="t.me/GPSiteInfoBot_Pro_Bot?startgroup=true")]]

# for test purposes
def error_callback(update: Update, context: CallbackContext):
    error = context.error
    try:
        raise error
    except Unauthorized:
        print("no nono1")
        print(error)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        print("no nono2")
        print("BadRequest caught")
        print(error)

        # handle malformed requests - read more below!
    except TimedOut:
        print("no nono3")
        # handle slow connection problems
    except NetworkError:
        print("no nono4")
        # handle other connection problems
    except ChatMigrated as err:
        print("no nono5")
        print(err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        print(error)
        # handle all other telegram related errors






def main():

    start_handler = CommandHandler("start", start)

    dispatcher.add_handler(start_handler)
    dispatcher.add_error_handler(error_callback)

    if WEBHOOK:
        LOGGER.info("Using webhooks.")
        updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)

        if CERT_PATH:
            updater.bot.set_webhook(url=URL + TOKEN, certificate=open(CERT_PATH, "rb"))
        else:
            updater.bot.set_webhook(url=URL + TOKEN)

    else:
        LOGGER.info("Using long polling.")
        updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)

    if len(argv) not in (1, 3, 4):
        telethn.disconnect()
    else:
        telethn.run_until_disconnected()

    updater.idle()


if __name__ == "__main__":
    LOGGER.info("Starting Telethon")
    telethn.start(bot_token=BOT_TOKEN)
    main()
