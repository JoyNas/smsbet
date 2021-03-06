# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'play_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('sms', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('when', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('pin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pins.Pin'], null=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Game'], null=True)),
            ('amount', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('wins', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=15, decimal_places=2)),
        ))
        db.send_create_signal(u'play', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'play_message')


    models = {
        u'game.club': {
            'Meta': {'object_name': 'Club'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['game.League']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'game.game': {
            'Meta': {'object_name': 'Game'},
            'away_side': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'away_game'", 'to': u"orm['game.Club']"}),
            'bet_expiry': ('django.db.models.fields.DateTimeField', [], {}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'game_date': ('django.db.models.fields.DateTimeField', [], {}),
            'home_side': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_game'", 'to': u"orm['game.Club']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'odds': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'result': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'game.league': {
            'Meta': {'object_name': 'League'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
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
        },
        u'play.message': {
            'Meta': {'object_name': 'Message'},
            'amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['game.Game']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pins.Pin']", 'null': 'True'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sms': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'when': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'wins': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '2'})
        }
    }

    complete_apps = ['play']