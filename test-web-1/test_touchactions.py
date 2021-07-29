# File ：test_touchactions.py
# Author ：miao
from time import sleep
from selenium import webdriver
from selenium.webdriver import TouchActions

class TestTouchActions:
    # 创建setup方法
    def setup(self):
        # 创建w3c
        opion = webdriver.ChromeOptions()
        opion.add_experimental_option("w3c",False)
        # 创建driver
        self.driver = webdriver.Chrome(options=opion)
        # 缓冲5s
        self.driver.implicitly_wait(5)
        # 窗口最大化
        self.driver.maximize_window()
    # 创建teardown方法
    def teardown(self):
        # 关闭dirver
        self.driver.quit()
    # 创建测试方法
    def test_touchactions(self):
        # 链接网址
        self.driver.get("https://www.baidu.com")
        # 定位输入框
        ele1 = self.driver.find_element_by_id("kw")
        # 定位搜索按钮
        ele2 = self.driver.find_element_by_id("su")
        # 点击搜索框并输入“selenium测试”
        ele1.click()
        ele1.send_keys("selenium测试")
        # 创建action
        action = TouchActions(self.driver)
        # 点击搜索并执行action
        action.tap(ele2).perform()
        # 滑动到底部并执行action
        action.scroll_from_element(ele1,0,10000).perform()
        # 创建action1，如果不新创建，到第二页还会滑动到底部
        action1 = TouchActions(self.driver)
        # 定位下一页按钮并点击
        self.driver.find_element_by_css_selector('#page .n').click()
        # 执行action
        action1.perform()
        # 等待3s
        sleep(3)