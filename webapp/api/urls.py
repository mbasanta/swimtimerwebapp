from django.conf.urls import patterns, url, include
from api import views

urlpatterns = patterns('',
    url(r'^$', 'api.views.api_root'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^latest-version/$',
        views.LatestVersionDetail.as_view(),
        name='latest-version'),

    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<username>[^/]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^teamsbyuser/(?P<username>[^/]+)/$',
        views.TeamsByUserList.as_view(),
        name='teams-by-user-list'),

    url(r'^groups/$',
        views.GroupList.as_view(),
        name='group-list'),
    url(r'^groups/(?P<name>[^/]+)/$',
        views.GroupDetail.as_view(),
        name='group-detail'),

    url(r'^meets/$',
        views.MeetList.as_view(),
        name='meet-list'),
    url(r'^meets/(?P<pk>[0-9]+)/$',
        views.MeetDetail.as_view(),
        name='meet-detail'),
    url(r'^meetsbyteam/(?P<team>[^/]+)/$',
        views.MeetByTeamList.as_view(),
        name='meet-by-team-list'),
)