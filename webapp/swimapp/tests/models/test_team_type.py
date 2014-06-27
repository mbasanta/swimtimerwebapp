'''tests for team_type'''
from django.test import TestCase
from swimapp.models.team_type import TeamType


class TeamTypeTest(TestCase):
    '''Test TeamType Class'''

    def test_unicode_method(self):
        '''Ensure unicode method returns string of type_name'''
        team_type = TeamType(type_abbr='NA', type_name='Name')
        self.assertEqual(str(team_type), team_type.type_name)
