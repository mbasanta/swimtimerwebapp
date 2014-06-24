""" Default urlconf for webapp """

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^o/', include('oauth2_provider.urls',
                        namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^swimapp/', include('swimapp.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^bad/$', bad),
    url(r'', include('base.urls')),
)

urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
