import importer
import unittest
import xmlrunner
import data.dictionary as dictionary

from common.test_case_utils import TestCaseUtils
from pages.login_page import LoginPage


class TS002FilterByTicketAndCity(unittest.TestCase):

    BROWSER = 'CHROME'  # Options: CHROME, FIREFOX, SAFARI
    HEAD_LESS = False
    page = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.utils = TestCaseUtils(cls)
        cls.user = cls.utils.config.get_user()
        cls.driver = cls.utils.open_browser()

    def test_01_main_test(self):
        self.page = LoginPage(self.driver, True, True)
        self.page = self.page.login(*self.user)

        self.page.click_view_settings()
        self.page.click_category(dictionary.categories["ticket_type"])
        self.page.click_option(dictionary.ticket_type["standard"])

        self.page.click_category(dictionary.categories["city"])
        self.page.search_option(dictionary.cities_full["andresfort"])
        self.page.click_option_strong(dictionary.cities_full["andresfort"])

        self.assertTrue(self.page.check_ticket_type(dictionary.ticket_type["standard"]),
                        "Not all the tickets are '" + dictionary.ticket_type["standard"] + "'")
        self.assertTrue(self.page.check_city(dictionary.cities["andresfort"]),
                        "Not all the tickets belong to the city '" + dictionary.cities["andresfort"] + "'")

    def setUp(self):
        self.utils.set_up(self)

    def tearDown(self):
        self.utils.tear_down(self)

    @classmethod
    def tearDownClass(cls):
        cls.utils.close()


if __name__ == '__main__':
    TestCaseUtils().set_parameters_to_test_case(TS002FilterByTicketAndCity)
    with open('reports/TS002FilterByTicketAndCity.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output, verbosity=2),
                      failfast=False, buffer=False, catchbreak=False)
