'''Classes related to Team'''
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from localflavor.us.models import USStateField, PhoneNumberField
from .team_registration import TeamRegistration
from .team_type import TeamType
from south.modelsinspector import add_introspection_rules

add_introspection_rules([], [r"^localflavor\.us\.models\.USStateField"])
add_introspection_rules([], [r"^localflavor\.us\.models\.PhoneNumberField"])


class TeamManager(models.Manager):  # pylint: disable=R0904
    '''Static classes related to teams'''

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def teams_for_user(self, user):  # pylint: disable=E1002
        '''Return a queryset fo teams that below to a user'''
        return super(TeamManager, self).get_queryset().filter(Q(users=user.id))


class Team(models.Model):
    '''Teams info'''
    # pylint: disable=C0330
    team_abbr = models.CharField("Team Abbreviation",
                                 max_length=5,
                                 help_text="Up to five characters to "
                                           "identify your team")
    team_name = models.CharField(max_length=30)
    team_short_name = models.CharField("Short Team Name",
                                       max_length=16)
    team_type = models.ForeignKey(TeamType)
    team_color1 = models.CharField(max_length=10,
                                   blank=True,
                                   null=True)
    team_color2 = models.CharField(max_length=10,
                                   blank=True,
                                   null=True)
    addr_name = models.CharField(max_length=30)
    addr = models.CharField(max_length=30)
    addr_city = models.CharField(max_length=30)
    addr_state = USStateField()
    addr_zip = models.CharField(max_length=10)
    addr_country = models.CharField(max_length=3)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    team_reg = models.ForeignKey(TeamRegistration)
    daytime_phone = PhoneNumberField(blank=True)
    evening_phone = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)
    email = models.CharField(max_length=36)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   verbose_name="Users that manage team")
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = TeamManager()

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
        return self.team_short_name

    def get_absolute_url(self):
        return reverse('swimapp_view_team', args=[self.id])
