# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Batch'
        db.create_table(u'pins_batch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'pins', ['Batch'])

        # Adding model 'Pin'
        db.create_table(u'pins_pin', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pin', self.gf('django.db.models.fields.CharField')(unique=True, max_length=16)),
            ('batch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pins.Batch'])),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'pins', ['Pin'])


    def backwards(self, orm):
        # Deleting model 'Batch'
        db.delete_table(u'pins_batch')

        # Deleting model 'Pin'
        db.delete_table(u'pins_pin')


    models = {
        u'pins.batch': {
            'Meta': {'object_name': 'Batch'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'pins.pin': {
            'Meta': {'object_name': 'Pin'},
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pins.Batch']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pin': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['pins']