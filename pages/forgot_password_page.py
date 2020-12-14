from locators.forgot_password_locators import ForgotPasswordLocators
from common.base_page import BasePage

import utils.logger as logger


class ForgotPasswordPage(BasePage):

    def __init__(self, driver, wait=True):
        """
        Initiates the Forgot Password page
        :wait: Boolean, waits for the elements in the page if True, default True
        """
        BasePage.__init__(self, driver)
        self.url = "/forgot-password"
        if wait:
            self.wait_til_element_is_clickable(ForgotPasswordLocators.title_txt)

    def is_page_loaded(self):
        """
        Verifies if the Forgot Password page is loaded
        :return: Boolean
        """
        logger.info("Verifying the Forgot Password page is displayed")
        return self.is_visible(ForgotPasswordLocators.title_txt)

    def wait_for_page_to_load(self):
        """
        Waits for the Forgot Password page to load
        """
        logger.info("Waiting for the Forgot Password page to load")
        self.wait_til_element_is_clickable(ForgotPasswordLocators.title_txt)