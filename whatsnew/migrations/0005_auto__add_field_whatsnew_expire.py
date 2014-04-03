# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'WhatsNew.expire'
        db.add_column(u'whatsnew_whatsnew', 'expire',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'WhatsNew.expire'
        db.delete_column(u'whatsnew_whatsnew', 'expire')


    models = {
        u'whatsnew.whatsnew': {
            'Meta': {'object_name': 'WhatsNew'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expire': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'version': ('whatsnew.fields.VersionField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['whatsnew']