'''tests for api teambyuser'''
# pylint: disable=E1101, E1103
import pytz
from datetime import datetime
from rest_framework import status
from rest_framework.test import APIClient
from base.models import AppUser
from selenium import webdriver
from swimapp.models.team import Team, TeamType, TeamRegistration
from swimapp.models.version import Version
from oauth2_provider.models import AccessToken, Application
import unittest


class TeamsByUserTest(unittest.TestCase):  # pylint: disable=R0904
    '''Test teamsbyuser api call'''

    def setUp(self):
        '''Setup tests'''
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer test_token')
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

        user = AppUser.objects.create(email='test@example.com')
        reg = TeamRegistration.objects.create(type_abbr='1', type_name='One')
        the_type = TeamType.objects.create(type_abbr='2', type_name='Two')
        team = Team.objects.create(
            team_abbr='abbr',
            team_name='team_name',
            team_short_name='team_short_name',
            team_type=the_type,
            team_color1='#111111',
            team_color2='#222222',
            addr_name='addr_name',
            addr='addr',
            addr_city='addr_city',
            addr_state='KY',
            addr_zip='40514',
            addr_country='USA',
            latitude=38.123,
            longitude=-84.123,
            team_reg=reg,
            daytime_phone='123-456-7890',
            evening_phone='987-123-4567',
            fax='567-1234-0987',
            email='test@example.com',
        )
        team.users_set = [user]
        team.save()

        app = Application.objects.create(
            client_id='client_id',
            user=user,
            client_type='Public',
            authorization_grant_type='Resource owner password-based'
        )

        AccessToken.objects.create(
            user=user,
            token='test_token',
            application=app,
            expires=datetime(year=2050, month=1, day=1, tzinfo=pytz.utc),
            scope='scope'
        )

        Version.objects.create(
            version=1,
            datetime=datetime.now(pytz.timezone('America/New_York'))
        )

    def tearDown(self):
        self.browser.quit()

    def test_api_valid_response(self):
        '''test api response data'''
        #user = AppUser.objects.get(email='test@example.com')
        response = self.client.get('/api/teamsbyuser/test@example.com/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get('/api/teamsbyuser/user/?test@example.com/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_not_authorized(self):
        '''test api if not authorized'''
        self.client = APIClient()
        response = self.client.get('/api/teamsbyuser/test@example.com/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.get('/api/teamsbyuser/user/?test@example.com/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
