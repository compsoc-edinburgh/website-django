# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Participant'
        db.create_table(u'ilwhack_participant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('real_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('matric', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('is_leader', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='members', null=True, to=orm['ilwhack.Team'])),
        ))
        db.send_create_signal(u'ilwhack', ['Participant'])

        # Adding model 'Team'
        db.create_table(u'ilwhack_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('project', self.gf('django.db.models.fields.related.OneToOneField')(related_name='leaderof', unique=True, null=True, to=orm['ilwhack.Project'])),
        ))
        db.send_create_signal(u'ilwhack', ['Team'])

        # Adding model 'Project'
        db.create_table(u'ilwhack_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('pitch', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('web', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('repo', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'ilwhack', ['Project'])


    def backwards(self, orm):
        # Deleting model 'Participant'
        db.delete_table(u'ilwhack_participant')

        # Deleting model 'Team'
        db.delete_table(u'ilwhack_team')

        # Deleting model 'Project'
        db.delete_table(u'ilwhack_project')


    models = {
        u'ilwhack.participant': {
            'Meta': {'object_name': 'Participant'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_leader': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'matric': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'real_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'members'", 'null': 'True', 'to': u"orm['ilwhack.Team']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        u'ilwhack.project': {
            'Meta': {'object_name': 'Project'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'pitch': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'repo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'ilwhack.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'leaderof'", 'unique': 'True', 'null': 'True', 'to': u"orm['ilwhack.Project']"})
        }
    }

    complete_apps = ['ilwhack']