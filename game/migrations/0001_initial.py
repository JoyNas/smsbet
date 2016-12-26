# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'League'
        db.create_table(u'game_league', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'game', ['League'])

        # Adding model 'Club'
        db.create_table(u'game_club', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('league', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.League'])),
        ))
        db.send_create_signal(u'game', ['Club'])

        # Adding model 'Game'
        db.create_table(u'game_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('home_side', self.gf('django.db.models.fields.related.ForeignKey')(related_name='home_game', to=orm['game.Club'])),
            ('away_side', self.gf('django.db.models.fields.related.ForeignKey')(related_name='away_game', to=orm['game.Club'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('game_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('odds', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('bet_expiry', self.gf('django.db.models.fields.DateTimeField')()),
            ('result', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'game', ['Game'])


    def backwards(self, orm):
        # Deleting model 'League'
        db.delete_table(u'game_league')

        # Deleting model 'Club'
        db.delete_table(u'game_club')

        # Deleting model 'Game'
        db.delete_table(u'game_game')


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
        }
    }

    complete_apps = ['game']