'''tests for meet_config'''
# pylint: disable=E1101
from django.test import TestCase
from swimapp.models.meet_config import MeetConfig


class MeetConfigTest(TestCase):  # pylint: disable=R0904
    '''Test MeetConfig Class'''

    def setUp(self):
        '''Setup tests'''
        MeetConfig.objects.create(type_name='One')
        MeetConfig.objects.create(type_name='Two')

    def test_objects_are_saved(self):
        '''Test objects are saved to the db'''
        configs = MeetConfig.objects.all()

        self.assertEqual(configs.count(), 2)
        self.assertEqual(configs[0].type_name, 'One')
        self.assertEqual(configs[1].type_name, 'Two')

    def test_unicode_method(self):
        '''Ensure unicode method returns string of type_name'''
        config = MeetConfig.objects.first()
        self.assertEqual(str(config), config.type_name)
