from django.db.models import signals
from sitecontacts.models import Contacts

class Sitecontactsapp(object):
    def __init__(self):
        self.cache_sitecontacts_latest = {}

        signals.post_save.connect(self.cache_flush, sender=Contacts)
        signals.post_delete.connect(self.cache_flush, sender=Contacts)

    def init_sitecontacts_latest(self):
        self.cache_sitecontacts_latest = list(Contacts.objects.filter(active=1, main=1))
        return self.cache_sitecontacts_latest

    def get_sitecontacts_latest(self):
        if len(self.cache_sitecontacts_latest) > 0:
            return self.cache_sitecontacts_latest
        else:
            return self.init_sitecontacts_latest()

    def sitecontacts_latest(self, context):
        return self.get_sitecontacts_latest()[0]

    def cache_flush(self, **kwargs):
        self.cache_sitecontacts_latest = {}

sitecontacts = Sitecontactsapp()
