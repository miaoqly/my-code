# File ：basepage.py
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from handle_black import handle_black


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        self.params = {}
    @handle_black
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

    def wait_for_click(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))

    def find_and_send_keys(self, locator, value):
        return self.find(locator).send_keys(value)

    def steps(self,page_path,operations):
        with open(page_path,"r",encoding="utf-8") as f:
            data = yaml.safe_load(f)
        steps = data[operations]
        for step in steps:
            if step["action"] == "find_and_send_keys":
                content: str = step["value"]
                for param in self.params:
                    content = content.replace("{%s}" % param, self.params[param])
                self.find_and_send_keys(step['locator'],content)
            elif step["action"] == "find_and_click":
                self.find_and_click(step['locator'])
            elif step["action"] == "wait_for_click":
                self.wait_for_click(step['locator'])
            elif step["action"] == "find_and_get_text":
                return self.find_and_get_text(step['locator'])
