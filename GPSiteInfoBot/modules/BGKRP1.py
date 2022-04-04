from GPSiteInfoBot import dispatcher

from GPSiteInfoBot.modules.helper_funcs.filters import CustomFilters

from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.ext import CallbackContext, CommandHandler
from telegram.utils.helpers import escape_markdown
from telegram import ParseMode, Update, InlineKeyboardButton, InlineKeyboardMarkup

Tower_Photo = "https://telegra.ph/file/3a093be342d6ff3e77221.jpg"

SITE_INFO_TEXT = """
📶 Site Code : BGKRP1

📶 Site Name : Karapara 1

📶 ISS_TYPE: Non-shared .

🌏 Site Location : Karapara, Dashani, Bagerhat.
"""

SITE_LOCATION_BUTTON = [[InlineKeyboardButton(text="🌍 Go to BGKRP1 site with maps", url="https://www.google.com/maps/place/22%C2%B038'19.0%22N+89%C2%B045'54.6%22E/@22.63861,89.76517,17z?gl=bd"),]]


def bgkrp1(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(Tower_Photo, SITE_INFO_TEXT, parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(SITE_LOCATION_BUTTON))


bkrp1_handler = CommandHandler("bgkrp1", bgkrp1, filters=CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(bkrp1_handler)
