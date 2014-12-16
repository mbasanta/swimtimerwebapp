'''Classes related to a finish place'''

# pylint: disable=C0103
# # Invalid variable name
# pylint: disable=R0903, R0904
# # Too few and too many public methods
# pylint: disable=E1120
# # No value in constructor call

from django.db import models
from swimapp.models.judge import Judge


class FinishPlaceManager(models.Manager):
    '''Static classes related to finish places'''

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def get_queryset(self):
        '''Override manager to use select related'''
        return super(FinishPlaceManager, self).get_queryset() \
            .select_related('entry')

    def create_from_serializer(self, finishplace_data, entry):
        '''get or create a dq from the serializer data'''
        judge = Judge.objects.create_from_serializer(finishplace_data['judge'])
        finishplace = self.create(
            finish_place=finishplace_data['finish_place'],
            entry=entry,
            judge=judge,)

        return finishplace


class FinishPlace(models.Model):
    '''finish place info'''
    finish_place = models.IntegerField()
    entry = models.ForeignKey('swimapp.Entry')
    judge = models.ForeignKey(Judge)
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = FinishPlaceManager()

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
        '''
        Define the __unicode__ method, which is used by related
        models by default.
        '''
        return unicode(self.finish_place)
