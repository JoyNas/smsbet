# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Game.result'
        db.alter_column(u'game_game', 'result', self.gf('django.db.models.fields.CharField')(default='', max_length=4))

    def backwards(self, orm):

        # Changing field 'Game.result'
        db.alter_column(u'game_game', 'result', self.gf('django.db.models.fields.PositiveIntegerField')(null=True))

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
        }
    }

    complete_apps = ['game']