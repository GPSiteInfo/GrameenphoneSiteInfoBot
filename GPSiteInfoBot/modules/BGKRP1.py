from GPSiteInfoBot import dispatcher


from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.ext import CallbackContext, CommandHandler
from telegram.utils.helpers import escape_markdown
from telegram import ParseMode, Update

SITE_INFO_TEXT = """
📶 Site Code : BGKRP1

📶 Site Name : Karapara 1

📶 ISS_TYPE: Non-shared .

🌏 Site Location : Karapara, Dashani, Bagerhat.
"""

SITE_LOCATION_BUTTON =  = [[InlineKeyboardButton(text="Go to site with maps", url="https://github.com/Al-Noman-Pro/GPSiteInfoBot"),]


dispatcher.run_async
def bgkrp1(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
            SITE_INFO_TEXT,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(SITE_LOCATION_BUTTON))


bkrp1_handler = CommandHandler("bgkrp1", bgkrp1)
dispatcher.add_handler(bkrp1_handler)
