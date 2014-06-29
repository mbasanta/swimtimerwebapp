'''tests for team class'''
# pylint: disable=E1101
from django.test import TestCase
from base.models import AppUser
from swimapp.models.team import Team, TeamType, TeamRegistration


class TeamsTest(TestCase):  # pylint: disable=R0904
    '''Test for team class'''

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
            email='test@example.com',
        )
        team.save()
        team.users = [user]
        team.save()

    def test_objects_are_saved(self):
        '''Test objects are saved to the db'''
        teams = Team.objects.all()

        self.assertEqual(teams.count(), 1)
        self.assertEqual(teams[0].team_name, 'team_name')

    def test_unicode_method(self):
        '''Ensure unicode method returns string of team_short_name'''
        team = Team.objects.first()
        self.assertEqual(str(team), team.team_short_name)

    def test_foreignkeys(self):
        '''Ensure foreign keys are working correctly'''
        team = Team.objects.first()
        self.assertEqual(str(team.team_type), 'Two')
        self.assertEqual(str(team.team_reg), 'One')
        self.assertEqual(team.users.all().count(), 1)
        self.assertEqual(team.users.first().email, 'test@example.com')

    def test_teams_for_user(self):
        '''test teams_for_user method'''
        teams = Team.objects.teams_for_user('test@example.com')
        self.assertEqual(teams.count(), 1)
        self.assertEqual(teams[0].team_name, 'team_name')
