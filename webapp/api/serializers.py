'''API serializers'''
# pylint: disable=E1123, E1120, R0903
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from swimapp.models.meet import Meet
from swimapp.models.event import Event
from swimapp.models.team import Team
from swimapp.models.entry import Entry
from swimapp.models.version import Version
from swimapp.models.athlete import Athlete
from swimapp.models.athlete_entry import AthleteEntry
from swimapp.models.facility import Facility
from swimapp.models.meet_event import MeetEvent
from rest_framework import serializers


class VersionSerializer(serializers.ModelSerializer):
    '''Serializer for Version class'''
    class Meta(object):
        '''Django Meta for VersionSerializer'''
        model = Version
        fields = ('version', 'datetime')
        lookup_field = None


class UserSerializer(serializers.ModelSerializer):
    '''Serializer for User class'''
    class Meta(object):
        '''Django meta for UserSerializer'''
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'groups')
        lookup_field = 'email'


class GroupSerializer(serializers.ModelSerializer):
    '''Serializer for Group class'''
    class Meta(object):
        '''Django meta for GroupSerializer'''
        model = Group
        fields = ('id', 'name')
        lookup_field = 'name'


class AthleteSerializer(serializers.ModelSerializer):
    '''Serializer for Athlete class'''
    class Meta(object):
        '''Django meta for AthleteSerializer'''
        model = Athlete
        fields = ('id', 'first_name', 'last_name', 'date_of_birth',
                  'gender', 'teams')


class AthleteEntrySerializer(serializers.ModelSerializer):
    '''Serializer for AthleteEntry class'''
    class Meta(object):
        '''Django meta for AthleteEntrySerializer'''
        model = AthleteEntry
        fields = ('athlete', 'athlete_order',)


class EntrySerializer(serializers.ModelSerializer):
    '''Serializer for Entry classs'''
    athleteentry_set = AthleteEntrySerializer(many=True)

    class Meta(object):
        '''Django meta for EventSerializer'''
        model = Entry
        fields = ('lane_number', 'seed_time', 'heat',
                  'athleteentry_set',)


class EventSerializer(serializers.ModelSerializer):
    '''Serializer for Event class'''
    entry_set = EntrySerializer(many=True)
    stroke = serializers.RelatedField(many=False)

    class Meta(object):
        '''Django meta for EventSerializer'''
        model = Event
        fields = ('id', 'event_name', 'lower_age', 'upper_age',
                  'gender', 'stroke', 'distance', 'distance_units',
                  'is_relay', 'entry_set')


class FacilitySerializer(serializers.ModelSerializer):
    '''Serializer for facility class'''
    length_1 = serializers.RelatedField()
    length_2 = serializers.RelatedField()

    class Meta(object):
        '''Django meta for FacilitySerializer'''
        model = Facility
        fields = ('facility_name', 'addr_name', 'addr', 'addr_city',
                  'addr_state', 'addr_zip', 'length_1', 'length_2',
                  'latitude', 'longitude', 'elevation')


class MeetEventSerializer(serializers.ModelSerializer):
    '''Serializer for meet event table'''
    event = EventSerializer()

    class Meta(object):
        '''Django meta for MeetEventSerializer'''
        model = MeetEvent
        fields = ('event_number', 'event')


class ShortTeamSerializer(serializers.ModelSerializer):
    '''Serializer for Team class without meet info'''

    class Meta(object):
        '''Django meta for TeamSerializer'''
        model = Team
        fields = ('id', 'team_name', 'team_abbr', 'team_color1', 'team_color2',
                  'addr_name', 'addr', 'addr_city', 'addr_state', 'addr_zip',
                  'addr_country')


class MeetSerializer(serializers.ModelSerializer):
    '''Serializer for all meet info and dependencies'''
    facility = FacilitySerializer()
    meetevent_set = MeetEventSerializer()
    meet_type = serializers.RelatedField(many=False)
    course_code_1 = serializers.RelatedField(many=False)
    course_code_2 = serializers.RelatedField(many=False)
    meet_config = serializers.RelatedField(many=False)
    athletes_for_meet = AthleteSerializer(many=True)
    teams_for_meet = ShortTeamSerializer(many=True)

    class Meta(object):
        '''Django meta for MeetSerializer'''
        model = Meet
        fields = ('id', 'meet_name', 'facility', 'start_date', 'end_date',
                  'age_up_date', 'meet_masters', 'meet_type',
                  'course_code_1', 'course_code_2', 'meet_config',
                  'meetevent_set', 'team', 'teams', 'athletes_for_meet',
                  'teams_for_meet')


class MeetListSerializer(serializers.ModelSerializer):
    '''Serializer for meets to give basic info for the list view'''

    class Meta(object):
        '''Django meta for MeetSerializer'''
        model = Meet
        fields = ('id', 'meet_name', 'facility', 'start_date', 'end_date',
                  'age_up_date', 'meet_masters', 'meet_type',
                  'course_code_1', 'course_code_2', 'meet_config',
                  'team', 'teams')


class ShortMeetSerializer(serializers.ModelSerializer):
    '''Serializer for basic meet info'''
    facility = serializers.RelatedField()
    meet_config = serializers.RelatedField(many=False)

    class Meta(object):
        '''Django meta for ShortMeetSerializer'''
        model = Meet
        fields = ('id', 'meet_name', 'facility', 'start_date', 'end_date',
                  'meet_config', 'age_up_date')


class TeamSerializer(serializers.ModelSerializer):
    '''Serializer for Team class'''
    meet_set = ShortMeetSerializer(many=True)
    all_meet_set = ShortMeetSerializer(many=True)

    class Meta(object):
        '''Django meta for TeamSerializer'''
        model = Team
        fields = ('id', 'team_name', 'team_abbr', 'team_color1', 'team_color2',
                  'addr_name', 'addr', 'addr_city', 'addr_state', 'addr_zip',
                  'addr_country', 'meet_set', 'all_meet_set')
