# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TrafficReport'
        db.create_table(u'traffiq_trafficreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('light', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('when', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'traffiq', ['TrafficReport'])


    def backwards(self, orm):
        # Deleting model 'TrafficReport'
        db.delete_table(u'traffiq_trafficreport')


    models = {
        u'traffiq.trafficreport': {
            'Meta': {'object_name': 'TrafficReport'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'light': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'when': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['traffiq']