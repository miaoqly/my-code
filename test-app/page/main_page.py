# File ：main_page.py
from appium.webdriver.common.mobileby import MobileBy
from page.addresslist_page import AddressListPage
from page.basepage import BasePage


class MainPage(BasePage):

    def goto_address_list(self):
        self.find_and_click((MobileBy.XPATH, "//*[@text='通讯录']"))
        return AddressListPage(self.driver)
