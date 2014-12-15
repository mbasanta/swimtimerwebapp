'''Views for Hydro.IO API'''

# pylint: disable=R0903, R0904
# # Too few and too many public methods
# pylint: disable=R0901
# # Too many ancestors

from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404
from swimapp.models import Meet, Event, Team, Version, Entry
from rest_framework import viewsets, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from api.serializers import (UserSerializer, GroupSerializer,
                             MeetSerializer, MeetListSerializer,
                             EventSerializer, TeamSerializer,
                             VersionSerializer, ResultEntrySerializer)
from api.renderers import SwimAppJSONRenderer


@api_view(('GET',))
def api_root(request, format=None):  # pylint: disable=W0622
    '''Boilerplate views for API, remove before production'''
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'groups': reverse('group-list', request=request, format=format),
        'meets': reverse('meet-list', request=request, format=format),
        'latest-version': reverse('latest-version',
                                  request=request, format=format),
    })


class LatestVersionDetail(generics.RetrieveAPIView):
    '''Retrieves the latest application version.'''
    serializer_class = VersionSerializer
    renderer_classes = (SwimAppJSONRenderer,)
    permission_classes = [permissions.IsAuthenticated, ]

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
    renderer_classes = (SwimAppJSONRenderer,)
    permission_classes = [permissions.IsAuthenticated, ]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, update or delete a user instance.'''
    User = get_user_model()
    lookup_field = 'email'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = (SwimAppJSONRenderer,)
    permission_classes = [permissions.IsAuthenticated, ]


class GroupList(generics.ListCreateAPIView):
    '''List all group, or create a new group.'''
    lookup_field = 'name'
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    renderer_classes = (SwimAppJSONRenderer,)
    permission_classes = [permissions.IsAuthenticated, ]


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, update or delete a group instance.'''
    lookup_field = 'name'
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    renderer_classes = (SwimAppJSONRenderer,)
    permission_classes = [permissions.IsAuthenticated, ]


class MeetList(generics.ListCreateAPIView):
    '''List all meet, or create a new meet.'''
    queryset = Meet.objects.all()
    renderer_classes = (SwimAppJSONRenderer,)
    serializer_class = MeetListSerializer
    permission_classes = [permissions.IsAuthenticated, ]  # TokenHasScope]
    #required_scopes = ['groups', 'write']


class MeetDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Retrieve, update or delete a meet instance.'''
    queryset = Meet.objects.all()
    renderer_classes = (SwimAppJSONRenderer,)
    serializer_class = MeetSerializer
    permission_classes = [permissions.IsAuthenticated, ]  # TokenHasScope]
    #required_scopes = ['groups', 'write']


class MeetByTeamList(generics.ListAPIView):
    '''List all meets for a given team'''
    serializer_class = MeetSerializer
    renderer_classes = (SwimAppJSONRenderer,)
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        '''Return list fo meets for a given team'''
        team = self.kwargs['team']
        return Meet.objects.filter(team=team)


class TeamsByUserList(generics.ListAPIView):
    '''List all teams for a given user'''
    serializer_class = TeamSerializer
    renderer_classes = (SwimAppJSONRenderer,)
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        '''Returns a list of teams for the given email'''
        try:
            email = self.kwargs['email']
        except KeyError:
            email = self.request.GET.get('email')
        return get_list_or_404(Team, users__email=email)


class EventViewSet(viewsets.ModelViewSet):
    '''Viewset for generic Event api views'''
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    renderer_classes = (SwimAppJSONRenderer,)
    permission_classes = [permissions.IsAuthenticated, ]


class TeamViewSet(viewsets.ModelViewSet):
    '''Viewset for generic team api views'''
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    renderer_classes = (SwimAppJSONRenderer,)
    permission_classes = [permissions.IsAuthenticated, ]


class ResultsUpload(generics.CreateAPIView):
    '''Upload results api endpoint view'''
    queryset = Entry.objects.all()
    serializer_class = ResultEntrySerializer
    permission_classes = [permissions.IsAuthenticated, ]
