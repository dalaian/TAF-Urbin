import datetime

from selenium.webdriver.common.keys import Keys

import utils.logger as logger
import time

from config import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    __IMPLICIT_WAIT = 10
    screen_shots_path = 'reports/screenshots'

    def __init__(self, driver):
        """
        Initiates the Base page
        """
        self.driver = driver
        self.browser_name = driver.capabilities['browserName']
        self.utilities = Config()

    """
    Several methods are encapsulated here because in this way they are easier to maintain, some browser updates
    create failures in one method and that may be fixed here.
    Also, to manage Safari, this is a good approach
    """

    # Common Actions

    def click(self, element):
        """
        Clicks on an element
        """
        # TODO: looks like selenium is not able to click a Safari element using elem.click(),
        #  so, click_js() is called instead. Check if this is absolute true
        if self.browser_name == 'Safari':
            self.click_js(element)
            return
        try:
            element = self.find_element(element)
            element.click()
        except Exception as ex:
            logger.error(ex)
            raise Exception(ex)

    def safe_click(self, element, timeout=__IMPLICIT_WAIT):
        """
        Clicks on an element but wait for it first
        """
        if self.browser_name == 'Safari':
            self.click_js(element, timeout)
            return
        try:
            self.wait_til_element_is_clickable(element, timeout)
            element = self.find_element(element)
            element.click()
        except Exception as ex:
            logger.error(ex)
            raise Exception(ex)

    def click_js(self, element, timeout=__IMPLICIT_WAIT):
        """
        Clicks on a element but using Javascript, which is almost certain it will click on it
        """
        try:
            self.wait_til_element_is_clickable(element, timeout)
            element = self.find_element(element)
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as ex:
            logger.error(ex)
            raise Exception(ex)

    def send_keys(self, element, keys, clear=True):
        """
        Send keys to a element, by the parameter clear you can clear the element before sending the keys
        :element: locator
        :keys: str
        :clear: Boolean, by default True
        """
        try:
            element = self.find_element(element)
            if clear:
                element.clear()
            element.send_keys(keys)
        except Exception as ex:
            logger.error(ex)
            raise Exception(ex)

    def send_keys_one_by_one(self, element, keys, clear=True):
        """
        Send keys in an element letter by letter. This is to cover the issues that sometimes the normal send_keys
        does not work properly
        """
        try:
            element = self.find_element(element)
            if clear:
                element.clear()
            for letter in keys:
                element.send_keys(letter)
                if self.browser_name == 'firefox':  # sometimes still fails on firefox
                    self.pause(0.1)
        except Exception as ex:
            logger.error(ex)
            raise Exception(ex)

    def get_text(self, element, timeout=__IMPLICIT_WAIT):
        """
        Gets the text of an element
        """
        try:
            self.wait_til_element_is_clickable(element, timeout)
            element = self.find_element(element)
            # Strip the text because safari does not do that
            return element.text.strip()
        except Exception as ex:
            logger.error(ex)
            raise Exception(ex)

    def get_attribute(self, element, attribute='value'):
        """
        Gets the value of an attribute of an element
        """
        try:
            element = self.find_element(element)
            return element.get_attribute(attribute)
        except Exception as ex:
            logger.error(ex)
            raise Exception(ex)

    # Checks

    def is_visible(self, element, timeout=__IMPLICIT_WAIT):
        """
        Checks if an element is visible (.is_displayed())
        """
        if self.wait_for_element(element, timeout):
            return self.find_element(element).is_displayed()
        return False

    def is_enabled(self, element, timeout=__IMPLICIT_WAIT):
        """
        Checks if an element is enabled
        """
        try:
            self.wait_for_element(element, timeout)
            element = self.find_element(element)
            return element.is_enabled()
        except Exception as ex:
            logger.error(ex)
            raise Exception(ex)

    # Waits

    def wait_for_element(self, element, timeout=__IMPLICIT_WAIT):
        """
        Waits for an element to be visible (visibility_of_element_located)
        """
        try:
            element = self.message_to_locator(element)
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(element))
        except Exception:
            logger.warn(self.wait_for_element, "Element " + str(element) + " was not found")
            return False
        return True

    def wait_til_element_is_clickable(self, element, timeout=__IMPLICIT_WAIT):
        """
        Waits for an element to be clickable (element_to_be_clickable)
        """
        try:
            element = self.message_to_locator(element)
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(element))
        except Exception:
            logger.warn(self.wait_til_element_is_clickable, "Element " + str(element) + " was not found")
            return False
        return True

    def pause(self, pause):
        """
        Explicit wait
        :pause: int, time in seconds
        """
        time.sleep(pause)

    # Basic Actions

    def find_element(self, element):
        """
        Finds an element and scroll to it to avoid issues
        """
        element = self.message_to_locator(element)
        element = self.driver.find_element(*element)
        return self.scroll_to_element(element)

    def find_elements(self, elements):
        """
        Finds elements
        """
        element = self.message_to_locator(elements)
        return self.driver.find_elements(*element)

    def message_to_locator(self, element):
        """
        Transform several types of locators to locators Selenium can use
        You can only send the xpath, the css selector, or a tuple with the By.ID and locator
        """
        if isinstance(element, basestring):
            if element.startswith('//'):
                return By.XPATH, element
            else:
                return By.CSS_SELECTOR, element

        if isinstance(element, tuple):
            return element

        return None

    def scroll_to_element(self, element):
        """
        Scroll to a given element. It's important to move to the element in case a screenshot is taken,
        otherwise the element may be not present in the screenshot
        :element: WebElement, element to go
        :return: WebElement
        """
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)
        return element

    # Browser

    def get(self, url):
        """
        Goes to a given URL
        """
        self.driver.get(url)

    def get_url(self):
        """
        Gets the current URL
        """
        logger.info("Getting the current url")
        return self.driver.current_url

    def refresh(self):
        """
        Refreshes the current page
        """
        logger.info("Refreshing the page")
        self.driver.refresh()

    # Extras

    def format(self, locator, value):
        """
        Format string, this is useful to format xpath with dynamic values
        """
        return locator.format(value)

    def take_screen_shot(self, name=None, screen_shot_dir=screen_shots_path):
        """
        Take an screen of the actual page in the browser
        :name: str, name of the screen, if not the date will be the name
        :screen_shot_dir: str, path to save the screenshot
        """
        # checks if a name was sent
        if name is None or len(name) <= 0:
            # if no name was sent, the name will be the date
            name = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        # creates the path for the screenshot
        path = '{}/{}_{}.png'.format(screen_shot_dir, name, self.browser_name)
        # takes the screenshot
        self.driver.save_screenshot(path)
        # logs where the screen was saved
        logger.info("Screenshot was saved in : " + path)

    # Logger
    # Creating this method here, allows to not import the logger in every page
    def logging(self, page, method):
        logger.auto_log(page, method)
