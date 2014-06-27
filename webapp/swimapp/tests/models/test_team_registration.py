'''tests for team_registration'''
from django.test import TestCase
from swimapp.models.team_registration import TeamRegistration


class TeamRegistrationTest(TestCase):  # pylint: disable=R0904
    '''Test TeamRegistration Class'''

    def test_unicode_method(self):
        '''Ensure unicode method returns string of type_name'''
        # pylint: disable=E1123, E1120
        registration = TeamRegistration(type_abbr='NA', type_name='Name')
        self.assertEqual(str(registration), registration.type_name)
