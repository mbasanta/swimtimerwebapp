from django.conf.urls import patterns, url, include
from api import views

urlpatterns = patterns('',
    url(r'^$', 'api.views.api_root'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<username>[^/]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),

    url(r'^groups/$',
        views.GroupList.as_view(),
        name='group-list'),
    url(r'^groups/(?P<name>[^/]+)/$',
        views.GroupDetail.as_view(),
        name='group-detail'),
)
