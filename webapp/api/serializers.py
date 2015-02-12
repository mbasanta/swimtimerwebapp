'''API serializers'''

# pylint: disable=R0903, R0904
# # Too few and too many public methods
# pylint: disable=W0142
# # Used * or ** magic
# pylint: disable=R0201
# # Method could be a function
# pylint: disable=W0223
# # Method is abstract but not overridden
# pylint: disable=C0103
# # Invalid property name

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from swimapp.models.athlete import Athlete
from swimapp.models.athlete_entry import AthleteEntry
from swimapp.models.entry import Entry
from swimapp.models.event import Event
from swimapp.models.facility import Facility
from swimapp.models.meet import Meet, MeetEvent
from swimapp.models.team import Team
from swimapp.models.version import Version
from swimapp.models.violation import Violation
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
        fields = ('id', 'athlete', 'athlete_order',)


class EntrySerializer(serializers.ModelSerializer):
    '''Serializer for Entry classs'''
    athleteentry_set = AthleteEntrySerializer(many=True)

    class Meta(object):
        '''Django meta for EventSerializer'''
        model = Entry
        fields = ('id', 'lane_number', 'seed_time', 'heat',
                  'override_order', 'athleteentry_set',)


class ResultJudgeSerializer(serializers.Serializer):
    '''Serializer for result judge'''
    username = serializers.CharField(max_length=50)
    is_authenticated = serializers.BooleanField()
    is_override = serializers.BooleanField()


class ResultDqSerializer(serializers.Serializer):
    '''Serializer for DQ reasons associated with a result'''
    judge = ResultJudgeSerializer()
    reason = serializers.CharField(max_length=50)
    violation_id = serializers.IntegerField()


class ResultFinishPlace(serializers.Serializer):
    '''Serializer for finish place'''
    judge = ResultJudgeSerializer()
    finish_place = serializers.IntegerField()


class ResultEntrySerializer(serializers.ModelSerializer):
    '''Serializer for uploading Entry results'''
    dq_set = ResultDqSerializer(many=True)
    finishplace_set = ResultFinishPlace(many=True)

    class Meta(object):
        '''Django meta for ResultEntrySerializer'''
        model = Entry
        fields = ('id', 'lane_number', 'heat', 'result_time', 'score',
                  'scoring_heat', 'dq_set', 'finishplace_set')

    def update(self, instance, validated_data):
        return Entry.objects.create_from_serializer(instance, validated_data)


class EventSerializer(serializers.ModelSerializer):
    '''Serializer for Event class'''
    stroke = serializers.StringRelatedField()

    class Meta(object):
        '''Django meta for EventSerializer'''
        model = Event
        fields = ('id', 'event_name', 'lower_age', 'upper_age', 'gender',
                  'stroke', 'distance', 'distance_units', 'is_relay')


class MeetEventSerializer(serializers.ModelSerializer):
    '''Serializer for MeetEvent class'''
    event = EventSerializer(many=False)
    entry_set = EntrySerializer(many=True)

    class Meta(object):
        '''Django meta for MeetEventSerializer'''
        model = MeetEvent
        fields = ('id', 'event', 'entry_set', 'event_number')


class FacilitySerializer(serializers.ModelSerializer):
    '''Serializer for facility class'''
    length_1 = serializers.StringRelatedField()
    length_2 = serializers.StringRelatedField()

    class Meta(object):
        '''Django meta for FacilitySerializer'''
        model = Facility
        fields = ('id', 'facility_name', 'addr_name', 'addr', 'addr_city',
                  'addr_state', 'addr_zip', 'length_1', 'length_2',
                  'lane_count_1', 'lane_count_2', 'latitude', 'longitude',
                  'elevation')


class ShortTeamSerializer(serializers.ModelSerializer):
    '''Serializer for Team class without meet info'''

    class Meta(object):
        '''Django meta for TeamSerializer'''
        model = Team
        fields = ('id', 'team_name', 'team_abbr', 'team_color1', 'team_color2',
                  'addr_name', 'addr', 'addr_city', 'addr_state', 'addr_zip',
                  'addr_country')


class ShortViolationSerializer(serializers.ModelSerializer):
    '''Serializer for violation summary for meet'''
    stroke = serializers.StringRelatedField()

    class Meta(object):
        '''Django meta for ShortViolationSerializer'''
        model = Violation
        fields = ('id', 'violation_number', 'server_id', 'stroke', 'title')


class MeetSerializer(serializers.ModelSerializer):
    '''Serializer for all meet info and dependencies'''
    facility = FacilitySerializer()
    meetevent_set = MeetEventSerializer(many=True)
    meet_type = serializers.StringRelatedField()
    course_code_1 = serializers.StringRelatedField()
    course_code_2 = serializers.StringRelatedField()
    meet_config = serializers.StringRelatedField()
    athletes_for_meet = AthleteSerializer(many=True)
    teams_for_meet = ShortTeamSerializer(many=True)
    violations_for_meet = ShortViolationSerializer(many=True)

    class Meta(object):
        '''Django meta for MeetSerializer'''
        model = Meet
        fields = ('id', 'meet_name', 'facility', 'start_date', 'end_date',
                  'age_up_date', 'meet_masters', 'meet_type',
                  'course_code_1', 'course_code_2', 'meet_config',
                  'max_entries', 'max_indiv_entries', 'max_relay_entries'
                  'lane_count', 'meetevent_set', 'team', 'teams',
                  'athletes_for_meet', 'teams_for_meet', 'violations_for_meet')


class MeetListSerializer(serializers.ModelSerializer):
    '''Serializer for meets to give basic info for the list view'''
    meet_type = serializers.StringRelatedField()
    course_code_1 = serializers.StringRelatedField()
    course_code_2 = serializers.StringRelatedField()
    meet_config = serializers.StringRelatedField()

    class Meta(object):
        '''Django meta for MeetSerializer'''
        model = Meet
        fields = ('id', 'meet_name', 'facility', 'start_date', 'end_date',
                  'age_up_date', 'meet_masters', 'meet_type',
                  'course_code_1', 'course_code_2', 'meet_config',
                  'max_entries', 'max_indiv_entries', 'max_relay_entries'
                  'lane_count', 'team', 'teams')


class ShortMeetSerializer(serializers.ModelSerializer):
    '''Serializer for basic meet info'''
    facility = serializers.StringRelatedField()
    meet_config = serializers.StringRelatedField()

    class Meta(object):
        '''Django meta for ShortMeetSerializer'''
        model = Meet
        fields = ('id', 'meet_name', 'facility', 'start_date', 'end_date',
                  'meet_config', 'age_up_date')


class TeamSerializer(serializers.ModelSerializer):
    '''Serializer for Team class'''
    meet_set = ShortMeetSerializer(many=True)

    class Meta(object):
        '''Django meta for TeamSerializer'''
        model = Team
        fields = ('id', 'team_name', 'team_abbr', 'team_color1', 'team_color2',
                  'addr_name', 'addr', 'addr_city', 'addr_state', 'addr_zip',
                  'addr_country', 'meet_set')
