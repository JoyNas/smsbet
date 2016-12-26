# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entry'
        db.create_table(u'emmob_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('phone1', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('phone2', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('curr_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('device_id', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'emmob', ['Entry'])


    def backwards(self, orm):
        # Deleting model 'Entry'
        db.delete_table(u'emmob_entry')


    models = {
        u'emmob.entry': {
            'Meta': {'object_name': 'Entry'},
            'curr_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'phone1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['emmob']