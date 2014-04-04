# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.template import Library
from django.utils.safestring import mark_safe
from whatsnew.util import display_message


register = Library()


@register.inclusion_tag('whatsnew/whatsnew.html', takes_context=True)
def whatsnew(context, package_name, force=1):
    cookie_name = "{}-whatsnew".format(package_name)

    display, news = display_message(context['request'], package_name, cookie_name)

    return {'name': cookie_name,
            'display': display or force,
            'news': news}
