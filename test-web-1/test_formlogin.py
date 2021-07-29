# File ：test_formlogin.py
# Author ：miao
from time import sleep
from selenium import webdriver


class TestFormLogin:
    def test_formlogin(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/account/sign_in")
        ele1 = self.driver.find_element_by_id("user_login")
        ele1.click()
        ele1.send_keys("miao")
        ele2 = self.driver.find_element_by_id("user_password")
        ele2.click()
        ele2.send_keys("233")
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[3]/div/label').click()
        self.driver.find_element_by_name("commit").click()
        sleep(5)