from django.conf.urls import patterns, url
from swimapp.views.team import TeamView, TeamCreate, TeamUpdate, TeamList


urlpatterns = patterns('swimapp.views',
    url(r'^team/$', TeamList.as_view(), name='swimapp_team_list'),
    url(r'^team/new/$', TeamCreate.as_view(), name='swimapp_new_team'),
    url(r'^team/(?P<pk>\d+)/$', TeamView.as_view(), name='swimapp_view_team'),
    url(r'^team/(?P<pk>\d+)/edit/$', TeamUpdate.as_view(),
        name='swimapp_edit_team'),
)
