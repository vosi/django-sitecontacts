from django import forms
from django.conf import settings
from sitecontacts.models import Contacts
from django.utils.translation import ugettext as _


class ContactsAdminForm(forms.ModelForm):
    tel = forms.RegexField(regex=r'^\+[0-9]{1,5} \([0-9]{2,6}\) [0-9-]{4,9}$',
                           help_text=_('Format: +1234 (12345) 123-45-67'))
    fax = forms.RegexField(regex=r'^\+[0-9]{1,5} \([0-9]{2,6}\) [0-9-]{4,9}$',
                           help_text=_('Format: +1234 (12345) 123-45-67'), required=False)

    class Meta:
        model = Contacts


class ContactsForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=80, required=True)
    email = forms.EmailField(label=_('Email'), max_length=80)
    phone = forms.RegexField(label=_('Phone'), regex=r'^\+[0-9]{1,5} \([0-9]{2,6}\) [0-9-]{4,9}$',
                             help_text=_('Format: +1234 (12345) 123-45-67'), required=False)
    message = forms.CharField(label=_('Message'), widget=forms.Textarea)

    class Media:
        js = (settings.STATIC_URL + "sitecontacts/js/jquery.form.js",
              settings.STATIC_URL + "sitecontacts/js/sitecontacts.js",)
