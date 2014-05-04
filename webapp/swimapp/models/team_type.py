'''Classes related to team types'''
from django.db import models


class TeamType(models.Model):
    '''Team types used for the domain in Team object'''
    type_abbr = models.CharField(max_length=3)
    type_name = models.CharField(max_length=50)

    class Meta:
        app_label = 'swimapp'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return self.type_name
