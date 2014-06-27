'''tests for team_config'''
from django.test import TestCase
from swimapp.models.meet_config import MeetConfig


class MeetConfigTest(TestCase):  # pylint: disable=R0904
    '''Test MeetConfig Class'''

    def test_unicode_method(self):
        '''Ensure unicode method returns string of type_name'''
        # pylint: disable=E1123, E1120
        meet_confgi = MeetConfig(type_name='Name')
        self.assertEqual(str(meet_confgi), meet_confgi.type_name)
