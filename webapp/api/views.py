from django.contrib.auth.models import User, Group
from django.http import Http404
from swimapp.models.meet import Meet
from swimapp.models.event import Event
from swimapp.models.team import Team
from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import UserSerializer, GroupSerializer
from api.serializers import MeetSerializer, EventSerializer
from api.serializers import TeamSerializer


class UserList(generics.ListCreateAPIView):
    """
    List all user, or create a new user.
    """
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user instance.
    """
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    lookup_field = 'name'
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MeetViewSet(viewsets.ModelViewSet):
    queryset = Meet.objects.all()
    serializer_class = MeetSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class UserByNameDetail(APIView):
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        user = self.get_object(username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
