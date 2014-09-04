'''test our views'''
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from base.views import home
# pylint: disable=R0904
#   Too many public methods
# pylint: disable=C0103
#   Invalid method name


class HomePageTest(TestCase):
    '''Home page view tests'''

    def test_root_url_resolves_to_home_page_view(self):
        '''test home page resolves correctly'''
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        '''make sure we get the correct html back'''
        request = HttpRequest()
        response = home(request)
        self.assertIn('<h1>Hello, world!</h1>', response.content)
