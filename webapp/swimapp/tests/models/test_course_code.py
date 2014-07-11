'''tests for course_code'''
# pylint: disable=E1101
from django.test import TestCase
from swimapp.models.course_code import CourseCode


class CourseCodeTest(TestCase):  # pylint: disable=R0904
    '''Test CourseCode Class'''

    def setUp(self):
        '''Setup tests'''
        CourseCode.objects.create(type_abbr='1', type_name='One')
        CourseCode.objects.create(type_abbr='2', type_name='Two')

    def test_objects_are_saved(self):
        '''Test objects are saved to the db'''
        codes = CourseCode.objects.all()

        self.assertEqual(codes.count(), 2)
        self.assertEqual(codes[0].type_name, 'One')
        self.assertEqual(codes[1].type_name, 'Two')

    def test_unicode_method(self):
        '''Ensure unicode method returns string of type_name'''
        code = CourseCode.objects.first()
        self.assertEqual(str(code), code.type_name)
