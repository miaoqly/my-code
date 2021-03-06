# File ：basepage.py
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def scroll_find_click(self, text):
        element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().'
            'scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().'
            f'text("{text}").instance(0));'
        )
        self.find_and_click(element)

    def find_and_get_text(self, locator):
        return self.find(locator).text

    def wait_for_click(self,locator,time):
        return WebDriverWait(self.driver,time).until(expected_conditions.element_to_be_clickable(locator))

    def find_and_send_keys(self,locator,value):
        return self.find(locator).send_keys(value)