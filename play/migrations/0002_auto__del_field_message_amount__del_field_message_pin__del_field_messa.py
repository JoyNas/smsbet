# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Message.amount'
        db.delete_column(u'play_message', 'amount')

        # Deleting field 'Message.pin'
        db.delete_column(u'play_message', 'pin_id')

        # Deleting field 'Message.wins'
        db.delete_column(u'play_message', 'wins')

        # Deleting field 'Message.game'
        db.delete_column(u'play_message', 'game_id')


    def backwards(self, orm):
        # Adding field 'Message.amount'
        db.add_column(u'play_message', 'amount',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Message.pin'
        db.add_column(u'play_message', 'pin',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pins.Pin'], null=True),
                      keep_default=False)

        # Adding field 'Message.wins'
        db.add_column(u'play_message', 'wins',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=15, decimal_places=2),
                      keep_default=False)

        # Adding field 'Message.game'
        db.add_column(u'play_message', 'game',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['game.Game'], null=True),
                      keep_default=False)


    models = {
        u'play.message': {
            'Meta': {'object_name': 'Message'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sender': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sms': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'when': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['play']