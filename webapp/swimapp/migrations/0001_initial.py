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
            ('team_color1', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('team_color2', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('addr_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('addr', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('addr_city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('addr_state', self.gf('localflavor.us.models.USStateField')(max_length=2)),
            ('addr_zip', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('addr_country', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
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
            ('appuser', models.ForeignKey(orm[u'base.appuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['team_id', 'appuser_id'])

        # Adding model 'AthleteEntry'
        db.create_table(u'swimapp_athleteentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('athlete', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.Athlete'])),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.Entry'])),
            ('athlete_order', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['AthleteEntry'])

        # Adding model 'Athlete'
        db.create_table(u'swimapp_athlete', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('time_entered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['Athlete'])

        # Adding M2M table for field teams on 'Athlete'
        m2m_table_name = db.shorten_name(u'swimapp_athlete_teams')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('athlete', models.ForeignKey(orm['swimapp.athlete'], null=False)),
            ('team', models.ForeignKey(orm['swimapp.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['athlete_id', 'team_id'])

        # Adding model 'MeetType'
        db.create_table(u'swimapp_meettype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_abbr', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('swimapp', ['MeetType'])

        # Adding model 'MeetConfig'
        db.create_table(u'swimapp_meetconfig', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('swimapp', ['MeetConfig'])

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

        # Adding model 'MeetEvent'
        db.create_table(u'swimapp_meetevent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.Meet'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.Event'])),
            ('event_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['MeetEvent'])

        # Adding model 'Event'
        db.create_table(u'swimapp_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lower_age', self.gf('django.db.models.fields.IntegerField')()),
            ('upper_age', self.gf('django.db.models.fields.IntegerField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('stroke', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.Stroke'])),
            ('distance', self.gf('django.db.models.fields.IntegerField')()),
            ('distance_units', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('is_relay', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('time_entered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['Event'])

        # Adding model 'Facility'
        db.create_table(u'swimapp_facility', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facility_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('elevation', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('length_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='length_1_set', null=True, to=orm['swimapp.CourseCode'])),
            ('length_2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='length_2_set', null=True, to=orm['swimapp.CourseCode'])),
            ('lane_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('addr_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('addr', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('addr_city', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('addr_state', self.gf('localflavor.us.models.USStateField')(max_length=2, null=True, blank=True)),
            ('addr_zip', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('addr_country', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('time_entered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['Facility'])

        # Adding model 'Meet'
        db.create_table(u'swimapp_meet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meet_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('facility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.Facility'])),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('age_up_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('meet_masters', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('meet_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='meet_type_set', null=True, to=orm['swimapp.MeetType'])),
            ('course_code_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='course_code_1_set', null=True, to=orm['swimapp.CourseCode'])),
            ('course_code_2', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='course_code_2_set', null=True, to=orm['swimapp.CourseCode'])),
            ('meet_config', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.MeetConfig'], null=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.Team'], null=True)),
            ('time_entered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['Meet'])

        # Adding unique constraint on 'Meet', fields ['meet_name', 'start_date']
        db.create_unique(u'swimapp_meet', ['meet_name', 'start_date'])

        # Adding M2M table for field teams on 'Meet'
        m2m_table_name = db.shorten_name(u'swimapp_meet_teams')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('meet', models.ForeignKey(orm['swimapp.meet'], null=False)),
            ('team', models.ForeignKey(orm['swimapp.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['meet_id', 'team_id'])

        # Adding model 'Version'
        db.create_table(u'swimapp_version', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version', self.gf('django.db.models.fields.IntegerField')()),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('swimapp', ['Version'])

        # Adding model 'Entry'
        db.create_table(u'swimapp_entry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lane_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('result_time', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('seed_time', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('heat', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('meetevent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['swimapp.MeetEvent'])),
            ('time_entered', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('swimapp', ['Entry'])


    def backwards(self, orm):
        # Removing unique constraint on 'Meet', fields ['meet_name', 'start_date']
        db.delete_unique(u'swimapp_meet', ['meet_name', 'start_date'])

        # Deleting model 'TeamRegistration'
        db.delete_table(u'swimapp_teamregistration')

        # Deleting model 'TeamType'
        db.delete_table(u'swimapp_teamtype')

        # Deleting model 'Team'
        db.delete_table(u'swimapp_team')

        # Removing M2M table for field users on 'Team'
        db.delete_table(db.shorten_name(u'swimapp_team_users'))

        # Deleting model 'AthleteEntry'
        db.delete_table(u'swimapp_athleteentry')

        # Deleting model 'Athlete'
        db.delete_table(u'swimapp_athlete')

        # Removing M2M table for field teams on 'Athlete'
        db.delete_table(db.shorten_name(u'swimapp_athlete_teams'))

        # Deleting model 'MeetType'
        db.delete_table(u'swimapp_meettype')

        # Deleting model 'MeetConfig'
        db.delete_table(u'swimapp_meetconfig')

        # Deleting model 'CourseCode'
        db.delete_table(u'swimapp_coursecode')

        # Deleting model 'Stroke'
        db.delete_table(u'swimapp_stroke')

        # Deleting model 'MeetEvent'
        db.delete_table(u'swimapp_meetevent')

        # Deleting model 'Event'
        db.delete_table(u'swimapp_event')

        # Deleting model 'Facility'
        db.delete_table(u'swimapp_facility')

        # Deleting model 'Meet'
        db.delete_table(u'swimapp_meet')

        # Removing M2M table for field teams on 'Meet'
        db.delete_table(db.shorten_name(u'swimapp_meet_teams'))

        # Deleting model 'Version'
        db.delete_table(u'swimapp_version')

        # Deleting model 'Entry'
        db.delete_table(u'swimapp_entry')


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
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['swimapp.Team']", 'symmetrical': 'False'}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'swimapp.athleteentry': {
            'Meta': {'object_name': 'AthleteEntry'},
            'athlete': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.Athlete']"}),
            'athlete_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.Entry']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'swimapp.coursecode': {
            'Meta': {'object_name': 'CourseCode'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type_abbr': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'type_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'swimapp.entry': {
            'Meta': {'object_name': 'Entry'},
            'athletes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['swimapp.Athlete']", 'through': "orm['swimapp.AthleteEntry']", 'symmetrical': 'False'}),
            'heat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lane_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'meetevent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.MeetEvent']"}),
            'result_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'seed_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'swimapp.event': {
            'Meta': {'object_name': 'Event'},
            'distance': ('django.db.models.fields.IntegerField', [], {}),
            'distance_units': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_relay': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lower_age': ('django.db.models.fields.IntegerField', [], {}),
            'stroke': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.Stroke']"}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'upper_age': ('django.db.models.fields.IntegerField', [], {})
        },
        'swimapp.facility': {
            'Meta': {'object_name': 'Facility'},
            'addr': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'addr_city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'addr_country': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'addr_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'addr_state': ('localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'addr_zip': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'facility_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lane_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'length_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'length_1_set'", 'null': 'True', 'to': "orm['swimapp.CourseCode']"}),
            'length_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'length_2_set'", 'null': 'True', 'to': "orm['swimapp.CourseCode']"}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'time_entered': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'swimapp.meet': {
            'Meta': {'unique_together': "(('meet_name', 'start_date'),)", 'object_name': 'Meet'},
            'age_up_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'course_code_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'course_code_1_set'", 'null': 'True', 'to': "orm['swimapp.CourseCode']"}),
            'course_code_2': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'course_code_2_set'", 'null': 'True', 'to': "orm['swimapp.CourseCode']"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'events': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['swimapp.Event']", 'through': "orm['swimapp.MeetEvent']", 'symmetrical': 'False'}),
            'facility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.Facility']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meet_config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.MeetConfig']", 'null': 'True'}),
            'meet_masters': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meet_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'meet_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'meet_type_set'", 'null': 'True', 'to': "orm['swimapp.MeetType']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['swimapp.Team']", 'null': 'True'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'all_meet_set'", 'symmetrical': 'False', 'to': "orm['swimapp.Team']"}),
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
            'event_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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