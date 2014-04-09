# -*- coding: utf-8 -*-
from __future__ import absolute_import
import datetime
from django.template import Library
from whatsnew.models import WhatsNew
from django.db.models import Q
from whatsnew.fields import Version
# from whatsnew.util import get_version


register = Library()


@register.inclusion_tag('whatsnew/whatsnew.html', takes_context=True)
def whatsnew(context, package_name, force=0):
    request = context['request']
    cookie_name = "{}-whatsnew".format(package_name)
    ctx = {'name': cookie_name}
    today = datetime.datetime.today()

    try:
        last = WhatsNew.objects.filter(enabled=True).filter(Q(expire__gte=today) | Q(expire=None)).latest()
        last_seen = Version(request.COOKIES.get(cookie_name) or '0.0')
        ctx.update({'content': last.content,
                    'version': last.version,
                    'display': (last.version > last_seen) or force})
    except WhatsNew.DoesNotExist:
        ctx.update({'content': None, 'version': None, 'display': force})

    return ctx
