# File ：contactedit_page.py
from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage


class ContactEditPage(BasePage):

    def edit_name(self,name):
        self.find_and_send_keys((MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText"),name)
        return self

    def edit_gender(self,gender):
        locator = (MobileBy.XPATH, "//*[@text='男']")
        ele = self.wait_for_click(locator,10)
        ele.click()
        if gender == '女':
            self.find_and_click((MobileBy.XPATH, "//*[@text='女']"))
        else:
            self.find_and_click((MobileBy.XPATH, "//*[@text='男']"))
        return self

    def edit_phone(self,phone):
        self.find_and_send_keys((MobileBy.ID, "com.tencent.wework:id/fwi"),phone)
        return self

    def click_save(self):
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/aj_"))
        from page.memberinvite_page import MemberInvitePage
        return MemberInvitePage(self.driver)
