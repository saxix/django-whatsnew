# -*- coding: utf-8 -*-
from django import forms
from django.contrib.admin import ModelAdmin, site
from whatsnew.models import WhatsNew

class EnhWidget(forms.Textarea):
    def __init__(self, attrs=None, editor_options=None):
        super(RedactorWidget, self).__init__(attrs)

try:
    from suit_redactor.widgets import RedactorWidget as EnhWidget
except ImportError:
    pass

try:
    from suit_ckeditor.widgets import CKEditorWidget as EnhWidget
except ImportError:
    pass


class WhatsNewForm(forms.ModelForm):
    class Meta:
        widgets = {
            'content': EnhWidget(editor_options={'lang': 'en'})
        }


class WhatsNewAdmin(ModelAdmin):
    # change_form_template = 'admin/whatsnew/change_form_whatsnew.html'
    list_display = ('version', 'date', 'expire', 'enabled')
    # form = WhatsNewForm
    # fieldsets = [
    #   ('Body', {'classes': ('full-width',), 'fields': ('content',)})
    # ]

site.register(WhatsNew, WhatsNewAdmin)
