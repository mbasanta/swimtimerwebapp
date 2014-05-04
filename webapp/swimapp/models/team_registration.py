'''Classes related to Team Registration'''
from django.db import models


class TeamRegistration(models.Model):
    '''Team registration used for domain in Team object'''
    type_abbr = models.CharField(max_length=4)
    type_name = models.CharField(max_length=50)

    class Meta:
        app_label = 'swimapp'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return self.type_name
