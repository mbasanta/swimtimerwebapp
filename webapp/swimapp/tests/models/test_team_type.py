'''tests for team_type'''
from django.test import TestCase
from swimapp.models.team_type import TeamType


class TeamTypeTest(TestCase):  # pylint: disable=R0904
    '''Test TeamType Class'''

    def test_unicode_method(self):
        '''Ensure unicode method returns string of type_name'''
        # pylint: disable=E1123, E1120
        team_type = TeamType(type_abbr='NA', type_name='Name')
        self.assertEqual(str(team_type), team_type.type_name)
