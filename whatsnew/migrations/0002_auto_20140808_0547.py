# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('whatsnew', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatsnew',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
