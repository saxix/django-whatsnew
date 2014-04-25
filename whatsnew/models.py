# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from .fields import VersionField
from django.utils.translation import gettext as _


class WhatsNew(models.Model):
    version = VersionField(order_field='order')
    date = models.DateField(default=datetime.today())
    content = models.TextField()
    expire = models.DateField(blank=True, null=True)
    enabled = models.BooleanField(default=False)
    order = models.CharField(max_length=150, default='', editable=False)

    def __unicode__(self):
        return unicode(self.version)

    class Meta:
        ordering = '-order',
        get_latest_by = 'order'
        verbose_name = _("What's New")
        verbose_name_plural = _("What's New")
