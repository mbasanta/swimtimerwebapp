'''tests for api teambyuser'''
# pylint: disable=E1101, E1103
import pytz
from datetime import datetime
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from base.models import AppUser
from swimapp.models.team import Team, TeamType, TeamRegistration
from swimapp.models.version import Version


class TeamsByUserTest(APITestCase):  # pylint: disable=R0904
    '''Test teamsbyuser api call'''

    def setUp(self):
        '''Setup tests'''
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
            email='none@example.com',
        )
        team.users_set = [user]
        team.save()

        Version.objects.create(
            version=1,
            datetime=datetime.now(pytz.timezone('America/New_York'))
        )

    def test_api_response_data(self):
        '''test api response data'''
        user = AppUser.objects.get(email='test@example.com')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get('/api/teamsbyuser/none@example.com/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
