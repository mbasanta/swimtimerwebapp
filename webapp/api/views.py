from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from swimapp.models.meet import Meet
from swimapp.models.event import Event
from swimapp.models.team import Team
from swimapp.models.version import Version
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from api.serializers import UserSerializer, GroupSerializer
from api.serializers import MeetSerializer, EventSerializer
from api.serializers import TeamSerializer
from api.serializers import VersionSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'groups': reverse('group-list', request=request, format=format),
        'meets': reverse('meet-list', request=request, format=format),
        'latest-version': reverse('latest-version', request=request, format=format),
    })


class LatestVersionDetail(generics.RetrieveAPIView):
    '''Retrieves the latest application version.'''
    serializer_class = VersionSerializer

    def get_queryset(self):
        '''Returns the versions'''
        return Version.objects.all()

    def get_object(self):
        '''Returns the latest application version'''
        queryset = self.get_queryset()
        return queryset.last()


class UserList(generics.ListCreateAPIView):
    '''List all user, or create a new user.'''
    User = get_user_model()
    lookup_field = 'email'
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, update or delete a user instance.'''
    User = get_user_model()
    lookup_field = 'email'
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListCreateAPIView):
    '''List all group, or create a new group.'''
    lookup_field = 'name'
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, update or delete a group instance.'''
    lookup_field = 'name'
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MeetList(generics.ListCreateAPIView):
    '''List all meet, or create a new meet.'''
    queryset = Meet.objects.all()
    serializer_class = MeetSerializer


class MeetDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, update or delete a meet instance.'''
    queryset = Meet.objects.all()
    serializer_class = MeetSerializer


class MeetByTeamList(generics.ListAPIView):
    '''List all meets for a given team'''
    serializer_class = MeetSerializer

    def get_queryset(self):
        '''Return list fo meets for a given team'''
        team = self.kwargs['team']
        return Meet.objects.filter(team=team)


class TeamsByUserList(generics.ListAPIView):
    '''List all teams for a given user'''
    serializer_class = TeamSerializer

    def get_queryset(self):
        '''Returns a list of teams for the given email'''
        try:
            email = self.kwargs['email']
        except KeyError:
            email = self.request.GET.get('email')
        return Team.objects.filter(users__email=email)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
