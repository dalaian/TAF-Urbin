from locators.login_locators import LoginLocators
from common.base_page import BasePage

import utils.logger as logger
import pages.forgot_password_page as forgot_password_page
import pages.dashboard.actions_page as actions_page


class LoginPage(BasePage):

    def __init__(self, driver, wait=True, go_to_page=False):
        """
        Initiates the Login page
        :wait: Boolean, waits for the elements in the page if True, default True
        :go_to_page: Boolean, goes to the page via URL if True, default False
        """
        BasePage.__init__(self, driver)
        self.url = "/login"
        if go_to_page:
            self.go_to_page(wait)
        elif wait:
            self.wait_for_page_to_load()

    def go_to_page(self, wait=True):
        """
        Goes directly to the Login page via URL
        :wait: Boolean, waits for the elements in the page if True, default True
        """
        logger.info("Going to the page '" + self.url + "'")
        self.get(self.utilities.get_base_url() + self.url)
        if wait:
            self.wait_til_element_is_clickable(LoginLocators.title_txt)

    def wait_for_page_to_load(self):
        """
        Waits for the login page to load
        """
        logger.info("Waiting for the Login Page to load")
        self.wait_til_element_is_clickable(LoginLocators.title_txt)

    def is_page_loaded(self):
        """
        Verifies if the login page is loaded
        :return: Boolean
        """
        logger.info("Verifying if the login page is loaded")
        return self.is_visible(LoginLocators.title_txt)

    def get_error_message(self):
        """
        Gets the error message displayed
        :return: str
        """
        logger.info("Getting the error message")
        return self.get_text(LoginLocators.error_msg)

    # Login

    def login(self, user, password, return_page=True):
        """
        Login the app, if you only want to login, use this method instead of the smaller ones
        :user: str
        :password: str
        :return_page: Boolean: return the corresponding page if True, default True
        """
        logger.info("login")
        self.enter_user(user)
        self.enter_password(password)
        return self.click_submit(return_page)

    def enter_user(self, user):
        """
        Enters the username
        :user: str
        """
        logger.info("Entering the user " + user)
        self.send_keys(LoginLocators.user_inp, user)

    def enter_password(self, password):
        """
        Enters the password
        :password: str
        """
        logger.info("Entering the password")  # TODO: not sure if logging the password is ok
        self.send_keys(LoginLocators.pass_inp, password)

    def click_submit(self, return_page=True):
        """
        Clicks on submit button
        :return_page: Boolean: return the Actions page if True, default True
        """
        logger.info("Clicking submit")
        self.click(LoginLocators.submit_btn)
        if return_page:
            return actions_page.ActionsPage(self.driver)

    # Forgot password

    def click_forgot_password(self, return_page=True):
        """
        Clicks on the forgot password link
        :return_page: Boolean: return the Forgot Password page if True, default True
        """
        logger.info("Clicking on forgot password")
        self.click(LoginLocators.forgot_pass_lnk)
        if return_page:
            return forgot_password_page.ForgotPasswordPage(self.driver)

    # Validations

    def is_submit_enabled(self):
        """
        Checks if the submit button is enabled
        :return: Boolean
        """
        logger.info("Verifying if the submit button is enabled")
        return self.is_enabled(LoginLocators.submit_btn)
