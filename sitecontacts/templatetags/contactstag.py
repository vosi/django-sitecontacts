from django import template
from sitecontacts.contactsapp import sitecontacts

register = template.Library()

@register.tag()
def sitecontacts_latest(parser, token):
    """
    {% sitecontacts_latest %}
    """
    return sitecontacts_latest_r()


class sitecontacts_latest_r(template.Node):
    def __init__(self):
        self.template = template.loader.get_template('sitecontacts/tags/widget.html')

    def render(self, context):
        widget_latest = sitecontacts.sitecontacts_latest(context)
        my_context = template.Context({'widget_latest': widget_latest})
        return self.template.render(my_context)

