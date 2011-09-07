from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _


class Contacts(models.Model):
    title = models.CharField(_('Title'), max_length=255)

    category = models.CharField(_('Category'), max_length=255)
    name = models.CharField(_('Name'), max_length=255)
    url = models.URLField(_('URL'), max_length=255)
    tel = models.CharField(_('Phone'), help_text=_('Format: +1234 (12345) 123-45-67'), max_length=255)
    fax = models.CharField(_('Fax'), help_text=_('Format: +1234 (12345) 123-45-67'), max_length=255, blank=True, null=True)
    email = models.EmailField(_('Email'), max_length=255)


    postal_code = models.CharField(_('Zip code'), max_length=7)
    country_name = models.CharField(_('Country'), max_length=255)
    region = models.CharField(_('Region'), max_length=255)
    locality = models.CharField(_('City'), max_length=255)
    street_address = models.CharField(_('Address'), max_length=255)
    geo_lat = models.DecimalField(_('Latitude'), max_digits=8, decimal_places=6, blank=True, null=True)
    geo_long = models.DecimalField(_('Longitude'), max_digits=8, decimal_places=6, blank=True, null=True)

    maplink = models.URLField(_('Link to map'), blank=True, null=True)

    main = models.BooleanField(_('Is main?'), default=True, db_index=True)


    active = models.BooleanField(_('Is active?'), default=True, db_index=True)
    created_at = models.DateTimeField(_('Date created'),
                                      auto_now_add=True, db_index=True,
                                      editable=False, default=datetime.now())
    created_by = models.ForeignKey(User, related_name='+',
                                   editable=False, blank=True,
                                   null=True, default=None)
    modified_at = models.DateTimeField(_('Date modified'),
                                       auto_now_add=True, auto_now=True, db_index=True,
                                       editable=False, default=datetime.now())
    modified_by = models.ForeignKey(User, related_name='+',
                                    editable=False, blank=True,
                                    null=True, default=None)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.main:
            self.__class__.objects.all().update(main=False)
            super(Contacts, self).save(*args, **kwargs)
        elif not self.main and self.__class__.objects.filter(main=True).count() == 0:
            t = self.__class__.objects.all()
            if (t.count() == 0):
                self.main = True
                super(Contacts, self).save(*args, **kwargs)
            else:
                super(Contacts, self).save(*args, **kwargs)
                self.__class__.objects.filter(pk=t[0].id).update(main=True)
        else:
            super(Contacts, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        if self.main:
            super(Contacts, self).delete(*args, **kwargs)
            t = self.__class__.objects.all()
            if (t.count() > 0):
                self.__class__.objects.filter(pk=t[0].id).update(main=True)
        else:
            super(Contacts, self).delete(*args, **kwargs)



    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
