from locators.dashboard.actions_locators import ActionsLocators
from common.base_page import BasePage

import utils.logger as logger


class ActionsPage(BasePage):

    def __init__(self, driver, wait=True):
        """
        Initiates the Actions page
        :wait: Boolean, waits for the elements in the page if True, default True
        """
        BasePage.__init__(self, driver)
        if wait:
            self.wait_for_page_to_load()

    def wait_for_page_to_load(self):
        """
        Waits for the Actions page to load
        """
        logger.info("Waiting for the Actions page to load")
        self.wait_til_element_is_clickable(ActionsLocators.title_txt)
        self.wait_until_table_displays_rows()

    def wait_until_table_displays_rows(self):
        """
        Waits for the table to display rows
        """
        logger.info("Waiting for table to display rows")
        self.wait_til_element_is_clickable(ActionsLocators.rows)

    def is_page_loaded(self):
        """
        Verify if the Actions page is loaded
        :return: Boolean
        """
        logger.info("Verifying if the Actions page is loaded")
        return self.is_visible(ActionsLocators.title_txt)

    def click_view_settings(self):
        """
        Clicks on the View Settings button
        """
        logger.info("Clicking view settings")
        self.click(ActionsLocators.view_setting_btn)
        self.wait_til_element_is_clickable(ActionsLocators.reset_view_btn)

    # Filter

    def click_category(self, category):
        """
        Clicks on a given category
        :category: str
        """
        logger.info("Clicking the category '" + category + "'")
        locator = self.format(ActionsLocators.category_p, category)
        self.safe_click(locator)
        self.pause(0.8)  # Gives a little time to load the animation of displaying the section

    def click_option(self, option):
        """
        Clicks on a given option
        :option: str
        """
        logger.info("Clicking the option '" + option + "'")
        locator = self.format(ActionsLocators.option_spn, option)
        self.safe_click(locator)
        self.pause(0.8)  # Gives a little time to avoid problems with the following wait
        self.wait_until_table_displays_rows()

    def click_option_strong(self, option):
        """
        Click on an option in Strong, the Strong text means the search matches.
        Take into consideration the app does not Strong the commas (,), so, that's why the text is split and uses
        the first part of the option.
        For instance "Brooklyn, NY" does not match because the app have the option in different tags, one for "Brooklyn"
        and another one for NY
        :option: str
        """
        logger.info("Clicking the option in strong '" + option + "'")
        if "," in option:
            option = option.split(",")[0]
        locator = self.format(ActionsLocators.option_selected_str, option)
        self.safe_click(locator)
        self.pause(0.8)  # Gives a little time to avoid problems with the following wait
        self.wait_until_table_displays_rows()

    def search_option(self, option):
        """
        Searches in the search input for a given option
        * The search input corresponding to the category should be displayed
        :option: str
        """
        logger.info("Searching for '" + option + "'")
        self.send_keys_one_by_one(ActionsLocators.search_inp, option)

    # Validations

    def check_ticket_type(self, ticket_type):
        """
        Checks if all the tickets displayed in the table are a given ticket type
        Logs all the tickets that are not the corresponding ticket type
        :ticket_type: str
        :return: Boolean
        """
        logger.info("Checking if all the displayed tickets are '" + ticket_type + "'")
        rows = self.find_elements(ActionsLocators.rows)
        result = True
        for row in rows:
            type_row = row.find_element(*ActionsLocators.row_type)
            if type_row.text != ticket_type:
                result = False
                ticket_number = row.find_element(*ActionsLocators.row_number).text
                logger.error("The ticket '" + ticket_number + "' is not type '" + ticket_type + "'")
        return result

    def check_city(self, city):
        """
        Checks if all the tickets displayed in the table are from a given city
        Logs all the tickets that are not from the corresponding city
        :city: str
        :return: Boolean
        """
        logger.info("Checking if all the displayed tickets are from the city'" + city + "'")
        rows = self.find_elements(ActionsLocators.rows)
        result = True
        for row in rows:
            type_row = row.find_element(*ActionsLocators.row_city)
            if type_row.text != city:
                result = False
                ticket_number = row.find_element(*ActionsLocators.row_number).text
                logger.error("The ticket '" + ticket_number + "' is not from the city'" + city + "'")
        return result
