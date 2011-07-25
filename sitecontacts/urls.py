from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'sitecontacts.views.form', name='sitecontacts-form'),
)



