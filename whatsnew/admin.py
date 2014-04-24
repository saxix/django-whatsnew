# -*- coding: utf-8 -*-
from django import forms
from django.contrib.admin import ModelAdmin, site
from whatsnew.models import WhatsNew

try:
    from suit_redactor.widgets import RedactorWidget
except ImportError:
    class RedactorWidget(forms.Textarea):
        def __init__(self, attrs=None, editor_options=None):
            super(RedactorWidget, self).__init__(attrs)


class WhatsNewForm(forms.ModelForm):
    class Meta:
        widgets = {
            'content': RedactorWidget(editor_options={'lang': 'en'})
        }


class WhatsNewAdmin(ModelAdmin):
    change_form_template = 'admin/whatsnew/change_form_whatsnew.html'
    list_display = ('version', 'date', 'expire', 'enabled')
    form = WhatsNewForm


site.register(WhatsNew, WhatsNewAdmin)
