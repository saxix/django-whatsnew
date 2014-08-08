# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import whatsnew.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WhatsNew',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('version', whatsnew.fields.VersionField(order_field=b'order', max_length=50)),
                ('date', models.DateField(default=datetime.datetime(2014, 8, 8, 5, 46, 50, 462543))),
                ('content', models.TextField()),
                ('expire', models.DateField(null=True, blank=True)),
                ('enabled', models.BooleanField(default=False)),
                ('order', models.CharField(max_length=150, default=b'', editable=False)),
            ],
            options={
                'verbose_name_plural': b"What's New",
                'get_latest_by': b'order',
                'ordering': (b'-order',),
                'verbose_name': b"What's New",
            },
            bases=(models.Model,),
        ),
    ]
