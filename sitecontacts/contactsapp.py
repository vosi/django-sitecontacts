from django.db.models import signals
from django.core.cache import cache
from sitecontacts.models import Contacts

CACHE_TIMEOUT = 3600 * 24 * 365 * 10


class Sitecontactsapp(object):
    def __init__(self):
        signals.post_save.connect(self.cache_flush, sender=Contacts)
        signals.post_delete.connect(self.cache_flush, sender=Contacts)

    def init_sitecontacts_latest(self):
        cache_sitecontacts_latest = list(Contacts.objects.filter(active=1, main=1))
        cache.set('cache_sitecontacts_latest', cache_sitecontacts_latest, CACHE_TIMEOUT)
        return cache_sitecontacts_latest

    def get_sitecontacts_latest(self):
        if cache.get('cache_sitecontacts_latest') != None:
            return cache.get('cache_sitecontacts_latest')
        else:
            return self.init_sitecontacts_latest()

    def sitecontacts_latest(self, context):
        if len(self.get_sitecontacts_latest()) > 0:
            return self.get_sitecontacts_latest()[0]
        else:
            return None

    def cache_flush(self, **kwargs):
        cache.delete('cache_sitecontacts_latest')

sitecontacts = Sitecontactsapp()
