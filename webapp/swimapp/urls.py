from django.conf.urls import patterns, url
from swimapp.views.team import TeamView, TeamCreate, TeamUpdate, TeamList
from swimapp.views.dashboard import DashboardView
from swimapp.views.fileupload import FileUploadCreate, FileUploadList
from swimapp.views.meet import MeetListView, MeetHy3File


urlpatterns = patterns('swimapp.views',
    url(r'^dashboard/$', DashboardView.as_view(), name='swimapp_user_dashboard'),
    url(r'^team/$', TeamList.as_view(), name='swimapp_team_list'),
    url(r'^team/new/$', TeamCreate.as_view(), name='swimapp_team_new'),
    url(r'^team/(?P<pk>\d+)/$', TeamView.as_view(), name='swimapp_team_view'),
    url(r'^team/(?P<pk>\d+)/edit/$', TeamUpdate.as_view(),
        name='swimapp_team_edit'),
    #url(r'^fileupload/$', FileUploadView.as_view(), name='swimapp_fileupload'),
    url(r'^fileupload/$', FileUploadList.as_view(),
        name='swimapp_file_upload_list'),
    url(r'^fileupload/new/$', FileUploadCreate.as_view(),
        name='swimapp_file_upload_new'),
    url(r'^meet/$', MeetListView.as_view(), name='swimapp_meet_list'),
    url(r'^meet/(?P<pk>\d+)/hy3file/$', MeetHy3File.as_view(), name='swimapp_meet_hy3file'),
)
