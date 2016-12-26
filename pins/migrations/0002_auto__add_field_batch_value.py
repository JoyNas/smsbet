# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Batch.value'
        db.add_column(u'pins_batch', 'value',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Batch.value'
        db.delete_column(u'pins_batch', 'value')


    models = {
        u'pins.batch': {
            'Meta': {'object_name': 'Batch'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
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