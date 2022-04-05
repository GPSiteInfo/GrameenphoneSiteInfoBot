from GPSiteInfoBot import dispatcher

from GPSiteInfoBot.modules.helper_funcs.filters import CustomFilters

from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.ext import CallbackContext, CommandHandler
from telegram.utils.helpers import escape_markdown
from telegram import ParseMode, Update, InlineKeyboardButton, InlineKeyboardMarkup

Tower_Photo = "https://telegra.ph/file/3a093be342d6ff3e77221.jpg"

SITE_INFO_TEXT = """
📶 Site Code: BGKML1

📶 Site Name: Pobontola Bazar

📶 ISS_TYPE: Seeker.

📶 Site Location: Pabontola Bazar, Rampal, Bagerhat.

"""

SITE_LOCATION_BUTTON = [[InlineKeyboardButton(text="✳ Go To BGKML1 Site With Maps", url="https://www.google.com/maps/dir/22.62167,89.68206"),]]


def bgkml1(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(Tower_Photo, SITE_INFO_TEXT, parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(SITE_LOCATION_BUTTON))


bgkml1_handler = CommandHandler("bgkml1", bgkml1, filters=CustomFilters.authorized_user, run_async=True)
dispatcher.add_handler(bgkml1_handler)
