from django.contrib import admin
from sitecontacts.forms import ContactsAdminForm
from sitecontacts.models import Contacts


class ContactsAdmin(admin.ModelAdmin):
    form = ContactsAdminForm

    actions = None
    actions_on_top = False
    actions_on_bottom = False
    save_on_top = True

    list_display = ('title','main',)
    list_per_page = 25
    ordering = ('id',)

    fieldsets = [
        (None, {'fields': ['title', ]}),
        (None, {'fields': ['category', 'name', ]}),
        (None, {'fields': ['url', 'tel', 'fax', 'email', ]}),
        (None, {'fields': ['country_name', 'postal_code', 'region', ]}),
        (None, {'fields': ['locality', 'street_address', ]}),
        (None, {'fields': ['geo_lat', 'geo_long', 'maplink' ]}),
        (None, {'fields': ['main', 'active' ]}),
    ]


admin.site.register(Contacts, ContactsAdmin)
