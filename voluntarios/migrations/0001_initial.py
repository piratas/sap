# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GTI'
        db.create_table(u'voluntarios_gti', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome_completo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cidade', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('telefone', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('cpf', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('skills', self.gf('django.db.models.fields.TextField')()),
            ('curriculum', self.gf('django.db.models.fields.files.FileField')(max_length=200)),
            ('linkedin', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('observacao', self.gf('django.db.models.fields.TextField')()),
            ('github', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('bitbucket', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gerenciar_projeto', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'voluntarios', ['GTI'])


    def backwards(self, orm):
        # Deleting model 'GTI'
        db.delete_table(u'voluntarios_gti')


    models = {
        u'voluntarios.gti': {
            'Meta': {'ordering': "['nome_completo']", 'object_name': 'GTI'},
            'bitbucket': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cidade': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cpf': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'curriculum': ('django.db.models.fields.files.FileField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'gerenciar_projeto': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nome_completo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'observacao': ('django.db.models.fields.TextField', [], {}),
            'skills': ('django.db.models.fields.TextField', [], {}),
            'telefone': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        }
    }

    complete_apps = ['voluntarios']