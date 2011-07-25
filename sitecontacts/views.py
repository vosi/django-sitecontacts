from django.core.mail.message import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext, Context
from django.template.loader import get_template
from django.utils import simplejson
from django.views.decorators.csrf import csrf_protect
from sitecontacts import settings
from sitecontacts.forms import ContactsForm
from sitecontacts.models import Contacts
from django.utils.translation import ugettext as _

@csrf_protect
def form(request):
    """
    @type request: django.http.HttpRequest
    """
    success = None
    contacts_list = list(Contacts.objects.filter(active=True).order_by('-main'))
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            success = settings.SUCCESS_MESSAGE
            textmail = get_template('sitecontacts/contacts_email.txt')
            context = Context({'from': form.cleaned_data['name'],
                               'email': form.cleaned_data['email'],
                               'phone': form.cleaned_data['phone'],
                               'message': form.cleaned_data['message']})
            subject, from_email, to = _('Email from site!'), form.cleaned_data['email'], settings.MAILTO
            textmail_content = textmail.render(context)
            msg = EmailMultiAlternatives(subject, textmail_content, from_email, [to])
            msg.send()

        if request.is_ajax():
            ret = {'fail': False}
            if not form.is_valid():
                ret.update({'fail': True})
                errs = {}
                for err in form.errors.iteritems():
                    errs.update({err[0]: unicode(err[1])})

                ret.update({'errs': errs})
            else:
                ret.update({'success': success})

            json = simplejson.dumps(ret, ensure_ascii=False)
            return HttpResponse(json, mimetype='application/json')
    else:
        form = ContactsForm()
    return render_to_response(
        'sitecontacts/contacts_all.html',
        {'form': form,
         'contacts_list': contacts_list,
         'success': success},
        context_instance=RequestContext(request),)


def text(a, b):
    return True
