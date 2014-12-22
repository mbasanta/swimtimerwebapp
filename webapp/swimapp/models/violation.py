'''Classes related to Team'''

# pylint: disable=R0903, R0904
# # Too few and too many public methods
# pylint: disable=W0142
# # Used * or ** magic
# pylint: disable=R0201
# # Method could be a function
# pylint: disable=C0103
# # Invalid property name

from django.db import models
from django.db.models import Q
from swimapp.models.meet import Meet
from swimapp.models.stroke import Stroke


class ViolationManager(models.Manager):
    '''Static classes related to violations'''

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def violations_for_meet(self, meet):
        '''Return a queryset fo teams that below to a user'''
        return super(ViolationManager, self).get_queryset().filter(
            Q(meet=meet)
        )


class Violation(models.Model):
    '''Violations info'''
    violation_number = models.IntegerField(
        blank=True,
        null=True)
    server_id = models.IntegerField(
        blank=True,
        null=True)
    stroke = models.ForeignKey(
        Stroke,
        blank=True,
        null=True)
    title = models.CharField(max_length=500)
    meets = models.ManyToManyField(Meet)
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = ViolationManager()  # pylint: disable=E1120

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
        return unicode(self.violation_number) + ': ' + self.title
