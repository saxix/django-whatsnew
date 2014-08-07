# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WhatsNew.order'
        db.add_column(u'whatsnew_whatsnew', 'order',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


        # Changing field 'WhatsNew.date'
        db.alter_column(u'whatsnew_whatsnew', 'date', self.gf('django.db.models.fields.DateField')())

    def backwards(self, orm):
        # Deleting field 'WhatsNew.order'
        db.delete_column(u'whatsnew_whatsnew', 'order')


        # Changing field 'WhatsNew.date'
        db.alter_column(u'whatsnew_whatsnew', 'date', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    models = {
        u'whatsnew.whatsnew': {
            'Meta': {'ordering': "('-version',)", 'object_name': 'WhatsNew'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 4, 25, 0, 0)'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expire': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'version': ('whatsnew.fields.VersionField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['whatsnew']