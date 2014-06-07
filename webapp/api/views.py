from django.contrib.auth.models import User, Group
from django.http import Http404
from swimapp.models.meet import Meet
from swimapp.models.event import Event
from swimapp.models.team import Team
from rest_framework import viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from api.serializers import UserSerializer, GroupSerializer
from api.serializers import MeetSerializer, EventSerializer
from api.serializers import TeamSerializer


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'groups': reverse('group-list', request=request, format=format),
    })


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


class GroupList(generics.ListCreateAPIView):
    """
    List all group, or create a new group.
    """
    lookup_field = 'name'
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a group instance.
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
