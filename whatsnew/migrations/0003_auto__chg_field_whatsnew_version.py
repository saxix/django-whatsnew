# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'WhatsNew.version'
        db.alter_column(u'whatsnew_whatsnew', 'version', self.gf('semantic_version.django_fields.VersionField')(max_length=200))

    def backwards(self, orm):

        # Changing field 'WhatsNew.version'
        db.alter_column(u'whatsnew_whatsnew', 'version', self.gf('django.db.models.fields.CharField')(max_length=30))

    models = {
        u'whatsnew.whatsnew': {
            'Meta': {'object_name': 'WhatsNew'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'released': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'version': ('semantic_version.django_fields.VersionField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['whatsnew']