# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WhatsNew'
        db.create_table(u'whatsnew_whatsnew', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'whatsnew', ['WhatsNew'])


    def backwards(self, orm):
        # Deleting model 'WhatsNew'
        db.delete_table(u'whatsnew_whatsnew')


    models = {
        u'whatsnew.whatsnew': {
            'Meta': {'object_name': 'WhatsNew'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['whatsnew']