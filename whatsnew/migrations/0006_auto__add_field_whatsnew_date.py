# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WhatsNew.date'
        db.add_column(u'whatsnew_whatsnew', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 4, 24, 0, 0), blank=True, auto_now_add=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WhatsNew.date'
        db.delete_column(u'whatsnew_whatsnew', 'date')


    models = {
        u'whatsnew.whatsnew': {
            'Meta': {'ordering': "('-date',)", 'object_name': 'WhatsNew'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expire': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'version': ('whatsnew.fields.VersionField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['whatsnew']