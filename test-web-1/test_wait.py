# File ：test_wait.py
# Author ：miao
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def test_wait(self):
        self.driver.find_element_by_xpath("//*[@id='ember41']").click()
        # def wait(x):
        #     return len(self.driver.find_elements_by_xpath("//*[@class='table-heading']")) >= 1
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))
        sleep(5)
        self.driver.find_element_by_xpath("//*[@title='在最近的一年，一月，一周或一天最活跃的主题']").click()
