from django.contrib.auth.models import User, Group
from swimapp.models.meet import Meet
from swimapp.models.event import Event
from swimapp.models.heat import Heat
from swimapp.models.team import Team
from swimapp.models.lane_assignment import LaneAssignment
from swimapp.models.version import Version
from rest_framework import serializers


class VersionSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Version
        fields = ('version', 'datetime')
        lookup_field = None


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ('id', 'username', 'email', 'groups')
        lookup_field = 'username'


class GroupSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Group
        fields = ('id', 'name')
        lookup_field = 'name'


class LaneAssignmentSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = LaneAssignment
        fields = ('lane_number', 'swimmer_name', 'uss_num')


class HeatSerializer(serializers.ModelSerializer):
    lane_assignments = LaneAssignmentSerializer(many=True)

    class Meta(object):
        model = Heat
        fields = ('heat_number', 'lane_assignments')


class EventSerializer(serializers.ModelSerializer):
    heats = HeatSerializer(many=True)
    stroke = serializers.RelatedField(many=False)

    class Meta(object):
        model = Event
        fields = ('id', 'event_name', 'event_number', 'lower_age', 'upper_age',
                  'stroke', 'distance', 'heats')


class MeetSerializer(serializers.ModelSerializer):
    '''Serializer for all meet info and dependencies'''
    events = EventSerializer(many=True)
    meet_type_1 = serializers.RelatedField(many=False)
    meet_type_2 = serializers.RelatedField(many=False)
    course_code_1 = serializers.RelatedField(many=False)
    course_code_2 = serializers.RelatedField(many=False)

    class Meta(object):
        model = Meet
        fields = ('id', 'meet_name', 'facility', 'start_date', 'end_date',
                  'age_up_date', 'elevation', 'meet_type_1', 'meet_type_2',
                  'course_code_1', 'course_code_2', 'events', 'team')


class ShortMeetSerializer(serializers.ModelSerializer):
    '''Serializer for basic meet info'''
    class Meta(object):
        model = Meet
        fields = ('id', 'meet_name', 'facility', 'start_date', 'end_date',
                  'age_up_date', 'elevation')


class TeamSerializer(serializers.ModelSerializer):
    meet_set = ShortMeetSerializer(many=True)

    class Meta(object):
        model = Team
        fields = ('id', 'team_name', 'team_abbr', 'team_color1', 'team_color2',
                  'addr_name', 'addr', 'addr_city', 'addr_state', 'addr_zip',
                  'addr_country', 'meet_set')
