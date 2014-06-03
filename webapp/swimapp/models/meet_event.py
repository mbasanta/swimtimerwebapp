'''Classes related to Meet Event ManyToMany relationships'''
from django.db import models
from django.core.urlresolvers import reverse


class MeetEventManager(models.Manager):  # pylint: disable=R0904
    '''Static classes related to meet events'''

    class Meta(object):  # pylint: disable=R0903
        '''Meta for model to be used by django'''
        app_label = 'swimapp'


class MeetEvent(models.Model):
    '''Meet Event info'''
    # Used the lazy reference method for the FK to avoid circular imports
    # http://stackoverflow.com/q/4379042/
    meet = models.ForeignKey('swimapp.Meet')
    event = models.ForeignKey('swimapp.Event')

    objects = MeetEventManager()  # pylint: disable=E1120

    class Meta:  # pylint: disable=R0903,W0232,C1001
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
    #Define the __unicode__ method, which is used by related models by default.
        return str(self.meet) + ' : ' + str(self.event)

    def get_absolute_url(self):  # pylint: disable=E0202
        '''Get reverse URL'''
        # pylint: disable=E1101
        return reverse('swimapp_view_meet_event', args=[self.id])
