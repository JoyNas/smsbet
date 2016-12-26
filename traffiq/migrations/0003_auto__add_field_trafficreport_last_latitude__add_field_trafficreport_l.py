# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TrafficReport.last_latitude'
        db.add_column(u'traffiq_trafficreport', 'last_latitude',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'TrafficReport.last_longitude'
        db.add_column(u'traffiq_trafficreport', 'last_longitude',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)

        # Adding field 'TrafficReport.speed'
        db.add_column(u'traffiq_trafficreport', 'speed',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TrafficReport.last_latitude'
        db.delete_column(u'traffiq_trafficreport', 'last_latitude')

        # Deleting field 'TrafficReport.last_longitude'
        db.delete_column(u'traffiq_trafficreport', 'last_longitude')

        # Deleting field 'TrafficReport.speed'
        db.delete_column(u'traffiq_trafficreport', 'speed')


    models = {
        u'traffiq.trafficreport': {
            'Meta': {'object_name': 'TrafficReport'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_latitude': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'last_longitude': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'speed': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'when': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['traffiq']