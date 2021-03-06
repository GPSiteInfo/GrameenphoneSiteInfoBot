from GPSiteInfoBot import dispatcher

from GPSiteInfoBot.modules.helper_funcs.filters import CustomFilters

from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.ext import CallbackContext, CommandHandler
from telegram.utils.helpers import escape_markdown
from telegram import ParseMode, Update, InlineKeyboardButton, InlineKeyboardMarkup

Tower_Photo = "https://telegra.ph/file/3a093be342d6ff3e77221.jpg"

SITE_INFO_TEXT = """
📶 Site Code: BGKRP1

📶 Site Name: Karapara 1.

📶 ISS_TYPE: Non-shared .

📶 Site Location: Karapara, Dashani, Bagerhat.
"""

SITE_LOCATION_BUTTON = [[InlineKeyboardButton(text="📶 Go To BGKRP1 Site With Maps", url="https://www.google.com/maps/place/22%C2%B037'24.3%22N+89%C2%B050'01.6%22E/@22.62342,89.83378,17z?gl=bd"),]]

def BGKRP1(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(Tower_Photo, SITE_INFO_TEXT, parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(SITE_LOCATION_BUTTON))


BGKRP1_handler = CommandHandler("BGKRP1", BGKRP1, run_async=True)
dispatcher.add_handler(BGKRP1_handler)
