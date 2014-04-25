# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'WhatsNew.order'
        db.alter_column(u'whatsnew_whatsnew', 'order', self.gf('django.db.models.fields.CharField')(max_length=150))

    def backwards(self, orm):

        # Changing field 'WhatsNew.order'
        db.alter_column(u'whatsnew_whatsnew', 'order', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'whatsnew.whatsnew': {
            'Meta': {'ordering': "('-order',)", 'object_name': 'WhatsNew'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 25, 0, 0)'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expire': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.CharField', [], {'max_length': '150', 'default': "''"}),
            'version': ('whatsnew.fields.VersionField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['whatsnew']