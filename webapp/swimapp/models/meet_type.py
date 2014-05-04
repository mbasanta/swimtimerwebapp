'''Classes related to meet types'''
from django.db import models


class MeetType(models.Model):
    '''Meet types used for the domain in Meet object'''
    type_abbr = models.CharField(max_length=2)
    type_name = models.CharField(max_length=50)

    class Meta:
        app_label = 'swimapp'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return self.type_name
