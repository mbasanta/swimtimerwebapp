'''tests for api teambyuser'''
import pytz
import json
from datetime import datetime
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from base.models import AppUser
from swimapp.models.team import Team, TeamType, TeamRegistration
from swimapp.models.version import Version
from oauth2_provider.models import AccessToken, Application

# pylint: disable=maybe-no-member, no-member
# pylint: disable=too-many-public-methods

class TeamsByUserTest(APITestCase):
    '''Test teamsbyuser api call'''

    def setUp(self):
        '''Setup tests'''
        self.client = APIClient()
        self.datetime_now = datetime.now(pytz.utc)


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
        team.users.add(user)
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
            expires=datetime(year=2050, month=1, day=1),
            scope='scope'
        )

        Version.objects.create(
            version=1,
            datetime=self.datetime_now
        )

    def test_api_without_parameter(self):
        '''test the api if an email isn't provided'''
        self.client.credentials(HTTP_AUTHORIZATION='Bearer test_token')

        response = self.client.get('/api/teamsbyuser/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = self.client.get('/api/teamsbyuser/none@none.com/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = self.client.get('/api/teamsbyuser/user/?email=none@na.com')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_api_authorized(self):
        '''test api response data'''
        self.client.credentials(HTTP_AUTHORIZATION='Bearer test_token')

        response = self.client.get('/api/teamsbyuser/test@example.com/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.get(
            '/api/teamsbyuser/user/?email=test@example.com')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_not_authorized(self):
        '''test api if not authorized'''
        self.client.credentials()

        response = self.client.get('/api/teamsbyuser/test@example.com/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        response = self.client.get('/api/teamsbyuser/user/?test@example.com/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_response_data(self):
        '''test to make sure response data is correct'''
        self.client.credentials(HTTP_AUTHORIZATION='Bearer test_token')
        data = [{
            "id":1, "team_name":"team_name", "team_abbr":"abbr", \
            "team_color1":"#111111", "team_color2":"#222222", \
            "addr_name":"addr_name", "addr":"addr", \
            "addr_city":"addr_city", "addr_state":"KY", \
            "addr_zip":"40514", "addr_country":"USA", "meet_set":[] \
        }]
        response = self.client.get(
            '/api/teamsbyuser/test@example.com/')
        alt_response = self.client.get(
            '/api/teamsbyuser/user/?email=test@example.com')
        self.assertEqual(response.rendered_content,
                         alt_response.rendered_content)
        self.assertEqual(response.data, data)
        response_json = json.loads(response.rendered_content)
        self.assertEqual(self.datetime_now.strftime('%Y-%m-%dT%H:%M:%SZ'),
                         response_json['timestamp'])
        self.assertEqual(response_json['version']['version_number'], 1)
        self.assertEqual(response_json['version']['version_date'],
                         self.datetime_now.strftime('%Y-%m-%dT%H:%M:%SZ'))
