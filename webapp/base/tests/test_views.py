'''test our views'''
from django.core.urlresolvers import resolve, reverse
from django.test import TestCase, Client
from base.views import home

# pylint: disable=too-many-public-methods
# pylint: disable=invalid-name
# pylint: disable=maybe-no-member


class HomePageTest(TestCase):
    '''Home page view tests'''

    def setUp(self):
        self.client = Client()

    def test_root_url_resolves_to_home_page_view(self):
        '''test home page resolves correctly'''
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        '''make sure we get the correct html back'''
        # request = HttpRequest()
        response = self.client.get(reverse('home'))
        # response = home(request)
        self.assertIn('Hydro.IO', response.content)
        self.assertEqual(response.status_code, 200)
