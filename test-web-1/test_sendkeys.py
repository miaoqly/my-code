# File ：test_sendkeys.py
# Author ：miao
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestSendKeys:
    # 定义setup方法
    def setup(self):
        # 创建driver
        self.driver = webdriver.Chrome()
        # 缓冲3s
        self.driver.implicitly_wait(3)
        # 窗口最大化
        self.driver.maximize_window()
    # 定义teardown方法
    def teardown(self):
        # 关闭driver
        self.driver.quit()
    # 定义测试方法
    def test_sendkeys(self):
        # 链接网址
        self.driver.get("http://sahitest.com/demo/label.htm")
        # 定位第一个输入框
        ele1 = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        # 点击第一个输入框
        ele1.click()
        # 创建action
        action = ActionChains(self.driver)
        # 向第一个输入框中输入：miao，等待1s
        action.send_keys("miao").pause(1)
        # 向第一个输入框中输入空格，等待1s
        action.send_keys(Keys.SPACE).pause(1)
        # 向第一个输入框中输入：ao，等待1s
        action.send_keys("ao").pause(1)
        # 删除：ao，等待1s
        action.send_keys(Keys.BACK_SPACE).send_keys(Keys.BACK_SPACE).send_keys(Keys.BACK_SPACE).pause(1)
        # 全选，等待1s
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
        # 复制，等待1s
        action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL)
        # 运行action
        action.perform()
        # 定位第二个输入框
        ele2 = self.driver.find_element_by_xpath("/html/body/label[2]/table/tbody/tr/td[2]/input")
        # 点击第二个输入框，等待1s
        ele2.click()
        # 粘帖，等待1s并运行action1
        action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        # 等待3s
        sleep(3)