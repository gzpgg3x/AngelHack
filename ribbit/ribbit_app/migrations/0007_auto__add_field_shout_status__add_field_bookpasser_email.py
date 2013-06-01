# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Shout.status'
        db.add_column(u'ribbit_app_shout', 'status',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=40, blank=True),
                      keep_default=False)

        # Adding field 'bookPasser.email'
        db.add_column(u'ribbit_app_bookpasser', 'email',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=18, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Shout.status'
        db.delete_column(u'ribbit_app_shout', 'status')

        # Deleting field 'bookPasser.email'
        db.delete_column(u'ribbit_app_bookpasser', 'email')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ribbit_app.bookpasser': {
            'Meta': {'object_name': 'bookPasser'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '18', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'ribbit_app.branch': {
            'Meta': {'object_name': 'Branch'},
            'branchaddress': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'branchname': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'branchphone': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ribbit_app.shout': {
            'Meta': {'object_name': 'Shout'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'book': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'branchname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'count': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        u'ribbit_app.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'follows': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'followed_by'", 'symmetrical': 'False', 'to': u"orm['ribbit_app.UserProfile']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['ribbit_app']