# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.template import Library
from types import StringTypes
import datetime
from whatsnew.models import WhatsNew
from django.db.models import Q
from whatsnew.fields import Version
from whatsnew.util import get_version


register = Library()


@register.inclusion_tag('whatsnew/whatsnew.html', takes_context=True)
def whatsnew(context, package_name, force=1):
    request = context['request']
    cookie_name = "{}-whatsnew".format(package_name)
    ctx = {'name': cookie_name}
    today = datetime.datetime.today()
    last = None

    last_seen = Version(request.COOKIES.get(cookie_name) or '0.0')
    current_version = Version(get_version(package_name))
    try:
        last = WhatsNew.objects.filter(enabled=True).filter(Q(expire__gte=today) | Q(expire=None)).latest()
        ctx.update({'content': last.content, 'version': last.version, 'display': True})
    except WhatsNew.DoesNotExist:
        ctx.update({'content': None, 'version': None, 'display': force})

    return ctx
