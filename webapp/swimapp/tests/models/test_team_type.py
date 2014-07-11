'''tests for team_type'''
# pylint: disable=E1101
from django.test import TestCase
from swimapp.models.team_type import TeamType


class TeamTypeTest(TestCase):  # pylint: disable=R0904
    '''Test TeamType Class'''

    def setUp(self):
        '''Setup tests'''
        TeamType.objects.create(type_abbr='1', type_name='One')
        TeamType.objects.create(type_abbr='2', type_name='Two')

    def test_objects_are_saved(self):
        '''Test objects are saved to the db'''
        types = TeamType.objects.all()

        self.assertEqual(types.count(), 2)
        self.assertEqual(types[0].type_name, 'One')
        self.assertEqual(types[1].type_name, 'Two')

    def test_unicode_method(self):
        '''Ensure unicode method returns string of type_name'''
        the_type = TeamType.objects.first()
        self.assertEqual(str(the_type), the_type.type_name)
