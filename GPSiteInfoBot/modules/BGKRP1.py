from GPSiteInfoBot import dispatcher


from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.ext import CallbackContext
from telegram.utils.helpers import escape_markdown
from telegram import ParseMode, Update

BGKRP1_TEXT = """
Hi ,I am Optimus Prime Bot.
I'm a group management bot.
"""

dispatcher.run_async
def bgkrp1(update: Update, context: CallbackContext):
    update.effective_message.reply_text(
                BGKRP1_TEXT.format(
                    escape_markdown(first_name), escape_markdown(context.bot.first_name)),
                parse_mode=ParseMode.MARKDOWN)



__help__ = """

*live cricket score*
*/cs* : Latest live scores from cricinfo.

*Get Fake details from fakenamegenerator.com*                             
*/fakeinfo* : returns fake information.

*GPS*
*/gps* <Place> : Show Location on a map.

*Image To Pdf*
*/pdf* : Reply to an image (as document) or group of images to make as pdf. 

*Show Json*
*/json* : Reply any message with /json .
 
*Style Text*
*/weebify* : Weebify Text.
*/square* : square Text.
*/blue* : Blues text.

*Zip - Unzip*
*/zip* : reply to a telegram file to compress it in .zip format.
*/unzip* : reply to a telegram file to decompress it from the .zip format.

"""
__mod_name__ = "BGKRP1"


bkrp1_handler = CommandHandler("bgkrp1", bgkrp1)
dispatcher.add_handler(bkrp1_handler)
