from django.conf import settings
from django.utils.translation import ugettext as _

SUCCESS_MESSAGE = getattr(settings, 'SITECONTACTS_SUCCESS_MESSAGE', _('Message sent!'))
MAILTO = getattr(settings, 'SITECONTACTS_MAILTO', getattr(settings, 'ADMINS')[0][1])
