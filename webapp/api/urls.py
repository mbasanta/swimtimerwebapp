from django.conf.urls import patterns, url, include
from rest_framework import routers
#from rest_framework.urlpatterns import format_suffix_patterns
from api import views

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
#router.register(r'meets', views.MeetViewSet)
#router.register(r'events', views.EventViewSet)
#router.register(r'teams', views.TeamViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    #url(r'^userbyname/(?P<username>[^/]+)/$', views.UserByNameDetail.as_view())
    url(r'^users/$', views.UserList.as_view()),
    #url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^users/(?P<username>[^/]+)/$', views.UserDetail.as_view()),
)
