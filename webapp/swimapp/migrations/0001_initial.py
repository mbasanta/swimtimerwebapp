# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TeamRegistration'
        db.create_table(u'swimapp_teamregistration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_abbr', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('swimapp', ['TeamRegistration'])

        # Adding model 'TeamType'
        db.create_table(u'swimapp_teamtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_abbr', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('swimapp', ['TeamType'])

        # Adding model 'Team'
        db.create_table(u'swimapp_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team_abbr', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('team_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('team_short_name', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('team_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.TeamType'])),
            ('addr_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('addr', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('addr_city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('addr_state', self.gf('localflavor.us.models.USStateField')(max_length=2)),
            ('addr_zip', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('addr_country', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('team_reg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.TeamRegistration'])),
            ('daytime_phone', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, blank=True)),
            ('evening_phone', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, blank=True)),
            ('fax', self.gf('localflavor.us.models.PhoneNumberField')(max_length=20, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('time_entered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['Team'])

        # Adding M2M table for field users on 'Team'
        m2m_table_name = db.shorten_name(u'swimapp_team_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('team', models.ForeignKey(orm['swimapp.team'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['team_id', 'user_id'])

        # Adding model 'MeetType'
        db.create_table(u'swimapp_meettype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_abbr', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('swimapp', ['MeetType'])

        # Adding model 'CourseCode'
        db.create_table(u'swimapp_coursecode', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_abbr', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('swimapp', ['CourseCode'])

        # Adding model 'Stroke'
        db.create_table(u'swimapp_stroke', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_abbr', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('swimapp', ['Stroke'])

        # Adding model 'Event'
        db.create_table(u'swimapp_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('event_number', self.gf('django.db.models.fields.IntegerField')()),
            ('lower_age', self.gf('django.db.models.fields.IntegerField')()),
            ('upper_age', self.gf('django.db.models.fields.IntegerField')()),
            ('stroke', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.Stroke'])),
            ('distance', self.gf('django.db.models.fields.IntegerField')()),
            ('time_entered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['Event'])

        # Adding model 'MeetEvent'
        db.create_table(u'swimapp_meetevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.Meet'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.Event'])),
        ))
        db.send_create_signal('swimapp', ['MeetEvent'])

        # Adding model 'Meet'
        db.create_table(u'swimapp_meet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meet_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('facility', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('age_up_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('elevation', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('meet_type_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='meet_type_1_set', to=orm['swimapp.MeetType'])),
            ('meet_type_2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='meet_type_2_set', to=orm['swimapp.MeetType'])),
            ('course_code_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='course_code_1_set', to=orm['swimapp.CourseCode'])),
            ('course_code_2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='course_code_2_set', to=orm['swimapp.CourseCode'])),
            ('time_entered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['Meet'])

        # Adding model 'Heat'
        db.create_table(u'swimapp_heat', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('heat_number', self.gf('django.db.models.fields.IntegerField')()),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(related_name='heats', to=orm['swimapp.Event'])),
            ('time_entered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['Heat'])

        # Adding model 'LaneAssignment'
        db.create_table(u'swimapp_laneassignment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lane_number', self.gf('django.db.models.fields.IntegerField')()),
            ('swimmer_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('uss_num', self.gf('django.db.models.fields.CharField')(max_length=14, blank=True)),
            ('heat', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lane_assignments', to=orm['swimapp.Heat'])),
            ('time_entered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['LaneAssignment'])


    def backwards(self, orm):
        # Deleting model 'TeamRegistration'
        db.delete_table(u'swimapp_teamregistration')

        # Deleting model 'TeamType'
        db.delete_table(u'swimapp_teamtype')

        # Deleting model 'Team'
        db.delete_table(u'swimapp_team')

        # Removing M2M table for field users on 'Team'
        db.delete_table(db.shorten_name(u'swimapp_team_users'))

        # Deleting model 'MeetType'
        db.delete_table(u'swimapp_meettype')

        # Deleting model 'CourseCode'
        db.delete_table(u'swimapp_coursecode')

        # Deleting model 'Stroke'
        db.delete_table(u'swimapp_stroke')

        # Deleting model 'Event'
        db.delete_table(u'swimapp_event')

        # Deleting model 'MeetEvent'
        db.delete_table(u'swimapp_meetevent')

        # Deleting model 'Meet'
        db.delete_table(u'swimapp_meet')

        # Deleting model 'Heat'
        db.delete_table(u'swimapp_heat')

        # Deleting model 'LaneAssignment'
        db.delete_table(u'swimapp_laneassignment')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'swimapp.coursecode': {
            'Meta': {'object_name': 'CourseCode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_abbr': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'swimapp.event': {
            'Meta': {'object_name': 'Event'},
            'distance': ('django.db.models.fields.IntegerField', [], {}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'event_number': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lower_age': ('django.db.models.fields.IntegerField', [], {}),
            'stroke': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.Stroke']"}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'upper_age': ('django.db.models.fields.IntegerField', [], {})
        },
        'swimapp.heat': {
            'Meta': {'object_name': 'Heat'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'heats'", 'to': "orm['swimapp.Event']"}),
            'heat_number': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'swimapp.laneassignment': {
            'Meta': {'object_name': 'LaneAssignment'},
            'heat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'lane_assignments'", 'to': "orm['swimapp.Heat']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lane_number': ('django.db.models.fields.IntegerField', [], {}),
            'swimmer_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uss_num': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'})
        },
        'swimapp.meet': {
            'Meta': {'object_name': 'Meet'},
            'age_up_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'course_code_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'course_code_1_set'", 'to': "orm['swimapp.CourseCode']"}),
            'course_code_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'course_code_2_set'", 'to': "orm['swimapp.CourseCode']"}),
            'elevation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['swimapp.Event']", 'through': "orm['swimapp.MeetEvent']", 'symmetrical': 'False'}),
            'facility': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meet_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'meet_type_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'meet_type_1_set'", 'to': "orm['swimapp.MeetType']"}),
            'meet_type_2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'meet_type_2_set'", 'to': "orm['swimapp.MeetType']"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'swimapp.meetevent': {
            'Meta': {'object_name': 'MeetEvent'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.Meet']"})
        },
        'swimapp.meettype': {
            'Meta': {'object_name': 'MeetType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_abbr': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'swimapp.stroke': {
            'Meta': {'object_name': 'Stroke'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_abbr': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'swimapp.team': {
            'Meta': {'object_name': 'Team'},
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'addr_city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'addr_country': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'addr_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'addr_state': ('localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'addr_zip': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'daytime_phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'evening_phone': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'blank': 'True'}),
            'fax': ('localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team_abbr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'team_reg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.TeamRegistration']"}),
            'team_short_name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'team_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.TeamType']"}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'})
        },
        'swimapp.teamregistration': {
            'Meta': {'object_name': 'TeamRegistration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_abbr': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'swimapp.teamtype': {
            'Meta': {'object_name': 'TeamType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_abbr': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['swimapp']