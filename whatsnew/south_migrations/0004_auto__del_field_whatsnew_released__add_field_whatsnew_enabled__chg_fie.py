# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'WhatsNew.released'
        db.delete_column(u'whatsnew_whatsnew', 'released')

        # Adding field 'WhatsNew.enabled'
        db.add_column(u'whatsnew_whatsnew', 'enabled',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'WhatsNew.version'
        db.alter_column(u'whatsnew_whatsnew', 'version', self.gf('whatsnew.fields.VersionField')(max_length=50))

    def backwards(self, orm):
        # Adding field 'WhatsNew.released'
        db.add_column(u'whatsnew_whatsnew', 'released',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'WhatsNew.enabled'
        db.delete_column(u'whatsnew_whatsnew', 'enabled')


    models = {
        u'whatsnew.whatsnew': {
            'Meta': {'object_name': 'WhatsNew'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'version': ('whatsnew.fields.VersionField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['whatsnew']
