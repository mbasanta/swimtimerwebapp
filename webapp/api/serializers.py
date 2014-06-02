from django.contrib.auth.models import User, Group
from swimapp.models.meet import Meet
from swimapp.models.event import Event
from swimapp.models.heat import Heat
from swimapp.models.team import Team
from swimapp.models.lane_assignment import LaneAssignment
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = Group
        fields = ('url', 'name')


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
        fields = ('event_name', 'event_number', 'lower_age', 'upper_age',
                  'stroke', 'distance', 'heats')


class MeetSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True)
    meet_type_1 = serializers.RelatedField(many=False)
    meet_type_2 = serializers.RelatedField(many=False)
    course_code_1 = serializers.RelatedField(many=False)
    course_code_2 = serializers.RelatedField(many=False)

    class Meta(object):
        model = Meet
        fields = ('meet_name', 'facility', 'start_date', 'end_date',
                  'age_up_date', 'elevation', 'meet_type_1', 'meet_type_2',
                  'course_code_1', 'course_code_2', 'events')


class TeamSerializer(serializers.ModelSerializer):
    meets = MeetSerializer(many=True)

    class Meta(object):
        model = Team
        fields = ('team_name', 'team_abbr', 'addr_name', 'addr', 'addr_city',
                  'addr_state', 'addr_zip', 'addr_country', 'meets')
