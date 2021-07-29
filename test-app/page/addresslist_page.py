# File ：addresslist_page.py
from appium.webdriver.common.mobileby import MobileBy
from page.basepage import BasePage
from page.memberinvite_page import MemberInvitePage

class AddressListPage(BasePage):

    def add_member(self):
        self.scroll_find_click("添加成员")
        return MemberInvitePage(self.driver)
