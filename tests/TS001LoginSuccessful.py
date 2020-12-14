import importer
import unittest
import xmlrunner
import data.login.TS001Login as data

from common.test_case_utils import TestCaseUtils
from pages.login_page import LoginPage


class TS001LoginSuccessful(unittest.TestCase):

    BROWSER = 'CHROME'  # Options: CHROME, FIREFOX, SAFARI
    HEAD_LESS = False
    page = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.utils = TestCaseUtils(cls)
        cls.user = cls.utils.config.get_user()
        cls.driver = cls.utils.open_browser()

    def test_01_navigation(self):
        self.__class__.page = LoginPage(self.driver, False, True)
        self.page.go_to_page()
        self.assertTrue(self.page.is_page_loaded())

    def test_02_empty_pass(self):
        self.page.enter_user(self.user[0])
        self.assertFalse(self.page.is_submit_enabled(), "The submit button is enabled")

    def test_03_empty_email(self):
        self.page.go_to_page()
        self.page.enter_password(self.user[1])
        self.assertFalse(self.page.is_submit_enabled(), "The submit button is enabled")

    def test_04_invalid_credentials(self):
        self.page.go_to_page()
        self.page.login(self.user[0], data.invalid_pass, False)
        self.assertEqual(self.page.get_error_message(), data.incorrect_credentials_msg,
                         "The error message is not correct")

    def test_05_forgot_password(self):
        # TODO: This may not belong here but can be moved to the correct section when created
        page = self.page.click_forgot_password()
        self.assertTrue(page.is_page_loaded(), "Forgot password page is not loaded")

    def test_06_valid_credentials(self):
        self.page.go_to_page()
        self.page = self.page.login(*self.user)
        self.assertTrue(self.page.is_page_loaded(), "The Actions page is not loaded")

    def setUp(self):
        self.utils.set_up(self)

    def tearDown(self):
        self.utils.tear_down(self)

    @classmethod
    def tearDownClass(cls):
        cls.utils.close()


if __name__ == '__main__':
    TestCaseUtils().set_parameters_to_test_case(TS001LoginSuccessful)
    with open('reports/TS001LoginSuccessful.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output, verbosity=2),
                      failfast=False, buffer=False, catchbreak=False)
