"""urlconf for the base application"""
# pylint: disable=C0103
from django.conf.urls import url, patterns


urlpatterns = patterns(
    'base.views',
    url(r'^$', 'home', name='home'),
)

urlpatterns += patterns(
    'django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'base/login.html'},
        name='swimapp_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='swimapp_logout'),
)
