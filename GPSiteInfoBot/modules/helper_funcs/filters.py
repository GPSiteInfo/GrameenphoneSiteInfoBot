from GPSiteInfoBot import OWNER_ID
from telegram import Message
from telegram.ext import MessageFilter


class CustomFilters(object):

    class _OwnerFilter(MessageFilter):
        def filter(self, message):
            return bool(message.from_user.id == OWNER_ID)

    owner_filter = _OwnerFilter()
