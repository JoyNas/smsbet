# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Entry'
        db.create_table(u'play_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['play.Message'])),
            ('pin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pins.Pin'], null=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Game'], null=True)),
            ('amount', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('wins', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=15, decimal_places=2)),
        ))
        db.send_create_signal(u'play', ['Entry'])


    def backwards(self, orm):
        # Deleting model 'Entry'
        db.delete_table(u'play_entry')


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
            'result': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'pins.pin': {
            'Meta': {'object_name': 'Pin'},
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pins.Batch']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pin': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'play.entry': {
            'Meta': {'object_name': 'Entry'},
            'amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['game.Game']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['play.Message']"}),
            'pin': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pins.Pin']", 'null': 'True'}),
            'wins': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '15', 'decimal_places': '2'})
        },
        u'play.message': {
            'Meta': {'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sms': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'when': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['play']