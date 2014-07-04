# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'LaneAssignment'
        db.delete_table(u'swimapp_laneassignment')

        # Adding model 'Entry'
        db.create_table(u'swimapp_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lane_number', self.gf('django.db.models.fields.IntegerField')()),
            ('result_time', self.gf('django.db.models.fields.FloatField')()),
            ('seed_time', self.gf('django.db.models.fields.FloatField')()),
            ('heat', self.gf('django.db.models.fields.related.ForeignKey')(related_name='entry', to=orm['swimapp.Heat'])),
            ('time_entered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['Entry'])

        # Adding model 'Athlete'
        db.create_table(u'swimapp_athlete', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('time_entered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['Athlete'])

        # Adding model 'AthleteEntry'
        db.create_table(u'swimapp_athleteentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('athlete', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.Athlete'])),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.Entry'])),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('swimapp', ['AthleteEntry'])

        # Adding field 'Event.distance_units'
        db.add_column(u'swimapp_event', 'distance_units',
                      self.gf('django.db.models.fields.CharField')(default='Y', max_length=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'LaneAssignment'
        db.create_table(u'swimapp_laneassignment', (
            ('heat', self.gf('django.db.models.fields.related.ForeignKey')(related_name='lane_assignments', to=orm['swimapp.Heat'])),
            ('uss_num', self.gf('django.db.models.fields.CharField')(max_length=14, blank=True)),
            ('swimmer_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('lane_number', self.gf('django.db.models.fields.IntegerField')()),
            ('time_entered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['LaneAssignment'])

        # Deleting model 'Entry'
        db.delete_table(u'swimapp_entry')

        # Deleting model 'Athlete'
        db.delete_table(u'swimapp_athlete')

        # Deleting model 'AthleteEntry'
        db.delete_table(u'swimapp_athleteentry')

        # Deleting field 'Event.distance_units'
        db.delete_column(u'swimapp_event', 'distance_units')


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
        u'base.appuser': {
            'Meta': {'object_name': 'AppUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'swimapp.athlete': {
            'Meta': {'object_name': 'Athlete'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'swimapp.athleteentry': {
            'Meta': {'object_name': 'AthleteEntry'},
            'athlete': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.Athlete']"}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.Entry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        'swimapp.coursecode': {
            'Meta': {'object_name': 'CourseCode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_abbr': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'swimapp.entry': {
            'Meta': {'object_name': 'Entry'},
            'heat': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entry'", 'to': "orm['swimapp.Heat']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lane_number': ('django.db.models.fields.IntegerField', [], {}),
            'result_time': ('django.db.models.fields.FloatField', [], {}),
            'seed_time': ('django.db.models.fields.FloatField', [], {}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'swimapp.event': {
            'Meta': {'object_name': 'Event'},
            'distance': ('django.db.models.fields.IntegerField', [], {}),
            'distance_units': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
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
        'swimapp.meet': {
            'Meta': {'object_name': 'Meet'},
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'addr_city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'addr_country': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'addr_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'addr_state': ('localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'addr_zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'age_up_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'course_code_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'course_code_1_set'", 'to': "orm['swimapp.CourseCode']"}),
            'course_code_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'course_code_2_set'", 'null': 'True', 'to': "orm['swimapp.CourseCode']"}),
            'elevation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['swimapp.Event']", 'through': "orm['swimapp.MeetEvent']", 'symmetrical': 'False'}),
            'facility': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'meet_config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.MeetConfig']"}),
            'meet_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'meet_type_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'meet_type_1_set'", 'to': "orm['swimapp.MeetType']"}),
            'meet_type_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'meet_type_2_set'", 'null': 'True', 'to': "orm['swimapp.MeetType']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.Team']"}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'swimapp.meetconfig': {
            'Meta': {'object_name': 'MeetConfig'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'team_abbr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'team_color1': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'team_color2': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'team_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'team_reg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.TeamRegistration']"}),
            'team_short_name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'team_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.TeamType']"}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.AppUser']", 'symmetrical': 'False'})
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
        },
        'swimapp.version': {
            'Meta': {'object_name': 'Version'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['swimapp']