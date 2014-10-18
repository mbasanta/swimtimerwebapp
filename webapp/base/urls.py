"""urlconf for the base application"""
# pylint: disable=C0103
from django.conf.urls import url, patterns
from base.views.appuser import (AppUserCreate, AppUserList, AppUserView,
                                AppUserUpdate)


urlpatterns = patterns(
    'base.views',
    url(r'^$', 'home', name='home'),
    url(r'^user/$', AppUserList.as_view(), name='base_appuser_list'),
    url(r'^user/new/$', AppUserCreate.as_view(), name='base_appuser_new'),
    url(r'^user/(?P<pk>\d+)/$', AppUserView.as_view(),
        name='base_appuser_view'),
    url(r'^user/(?P<pk>\d+)/edit/$', AppUserUpdate.as_view(),
        name='base_appuser_edit'),
)

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'base/login.html'},
        name='swimapp_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='swimapp_logout'),
)
