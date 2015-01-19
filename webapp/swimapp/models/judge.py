'''Classes related to judge'''

# pylint: disable=R0903, R0904
# # Too few and too many public methods
# pylint: disable=E1120
# # No value in constructor call

from django.conf import settings
from django.db import models
from base.models import AppUser


class JudgeManager(models.Manager):
    '''Static classes related to judge'''

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def create_from_serializer(self, judge_data):
        '''get or create a judge from the serializer data'''
        judge, new_judge = self.get_or_create(  # pylint:disable=W0612
            username=judge_data['username'],
            is_authenticated=judge_data['is_authenticated'],
            is_override=judge_data['is_override'],)

        try:
            user = AppUser.objects.get(email=judge.username)
            judge.user = user
        except AppUser.DoesNotExist:  # pylint:disable=E1101
            judge.user = None

        judge.save()

        return judge


class Judge(models.Model):
    '''Judge info'''
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True)
    username = models.CharField(
        max_length=50,
        blank=True,
        null=True)
    is_authenticated = models.BooleanField()
    is_override = models.BooleanField()
    time_entered = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    objects = JudgeManager()

    class Meta(object):
        '''Meta for model to be used by django'''
        app_label = 'swimapp'

    def __unicode__(self):
        '''
        Define the __unicode__ method, which is used by related
        models by default.
        '''
        return self.username
