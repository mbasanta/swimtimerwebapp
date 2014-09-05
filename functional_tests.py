'''functional tests for the website'''
from config import Config
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
# pylint: disable=R0904
#   Too many public methods


class NewVisitorTest(unittest.TestCase):
    '''Main functional tests'''

    def __log_out(self):
        '''Log out if needed, else do nothing'''
        try:
            self.browser.find_element_by_id('dropuser').click()
            self.browser.find_element_by_id('logoutuser').click()
        except NoSuchElementException:
            pass

    def __log_in(self):
        '''Log in if needed, else do nothing'''
        try:
            self.browser.find_element_by_name('username') \
                .send_keys(self.config['username'])
            self.browser.find_element_by_name('password') \
                .send_keys(self.config['password'])
            self.browser.find_element_by_id('login-submit').click()
        except NoSuchElementException:
            pass

    @classmethod
    def setUpClass(cls):
        cls.config = Config('testing.cfg')

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.browser.get(self.config['server'])

    def tearDown(self):
        self.browser.quit()

    def test_user_can_login(self):
        '''
        Test the homepage loads correctly from template and user can
        login
        '''
        self.__log_out()
        self.assertIn('Clepsydra Swim', self.browser.title)
        self.__log_in()
        navbars = self.browser.find_elements_by_class_name('navbar')
        self.assertTrue(
            any(self.config['username'] in nav.text for nav in navbars)
        )

    def test_user_can_add_team(self):
        '''test that user can add team successfully'''
        pass


if __name__ == '__main__':
    unittest.main()
