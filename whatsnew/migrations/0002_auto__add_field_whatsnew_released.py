# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WhatsNew.released'
        db.add_column(u'whatsnew_whatsnew', 'released',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WhatsNew.released'
        db.delete_column(u'whatsnew_whatsnew', 'released')


    models = {
        u'whatsnew.whatsnew': {
            'Meta': {'object_name': 'WhatsNew'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'released': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['whatsnew']