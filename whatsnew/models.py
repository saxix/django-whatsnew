# -*- coding: utf-8 -*-
from django.db import models
from .fields import VersionField
from django.utils.translation import gettext as _


class WhatsNew(models.Model):
    version = VersionField()
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    expire = models.DateField(blank=True, null=True)
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return unicode(self.version)

    class Meta:
        ordering = '-version',
        get_latest_by = 'date'
        verbose_name = _("What's New")
        verbose_name_plural = _("What's New")
