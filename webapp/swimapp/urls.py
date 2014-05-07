from django.conf.urls import patterns, include, url


urlpatterns = patterns("swimapp.views",
    url(r"^team/new/$", "edit_team", name="swimapp_new_team"),
    url(r"^team/(?P<pk>\d+)/$", "view_team", name="swimapp_view_team"),
    url(r"^team/(?P<pk>\d+)/edit/$", "edit_team", name="swimapp_edit_team"),
)
