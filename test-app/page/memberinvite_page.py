from appium.webdriver.common.mobileby import MobileBy
from page.basepage import BasePage
from page.contactedit_page import ContactEditPage


class MemberInvitePage(BasePage):

    def add_contact_menu(self):
        self.find_and_click((MobileBy.ID, "com.tencent.wework:id/cth"))
        return ContactEditPage(self.driver)

    def get_toast(self):
        toast = self.find_and_get_text((MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        print(f"提示是：{toast}")
        return toast
