# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TrafficReport.light'
        db.delete_column(u'traffiq_trafficreport', 'light')

        # Adding field 'TrafficReport.response'
        db.add_column(u'traffiq_trafficreport', 'response',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'TrafficReport.light'
        db.add_column(u'traffiq_trafficreport', 'light',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10),
                      keep_default=False)

        # Deleting field 'TrafficReport.response'
        db.delete_column(u'traffiq_trafficreport', 'response')


    models = {
        u'traffiq.trafficreport': {
            'Meta': {'object_name': 'TrafficReport'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'when': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['traffiq']