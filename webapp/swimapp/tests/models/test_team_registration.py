'''tests for team_registration'''
# pylint: disable=E1101
from django.test import TestCase
from swimapp.models.team_registration import TeamRegistration


class TeamRegistrationTest(TestCase):  # pylint: disable=R0904
    '''Test TeamRegistration Class'''

    def setUp(self):
        '''Setup tests'''
        TeamRegistration.objects.create(type_abbr='1', type_name='One')
        TeamRegistration.objects.create(type_abbr='2', type_name='Two')

    def test_objects_are_saved(self):
        '''Test objects are saved to the db'''
        registrations = TeamRegistration.objects.all()

        self.assertEqual(registrations.count(), 2)
        self.assertEqual(registrations[0].type_name, 'One')
        self.assertEqual(registrations[1].type_name, 'Two')

    def test_unicode_method(self):
        '''Ensure unicode method returns string of type_name'''
        registration = TeamRegistration.objects.first()
        self.assertEqual(str(registration), registration.type_name)
