# File ：base.py
# Author ：miao
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
# 定义基本类，用来放公共代码
class Base:
    # 声明url为空
    b_url = ""
    # 创建初始化构造方法，参数传递_driver设置为None
    def __init__(self,_driver:WebDriver=None):
        # 声明driver为空
        self.driver = ""
        # 如果_dirver是None，新建一个谷歌dirver
        if _driver is None:
            self.driver = webdriver.Chrome()
        else:
            # 如果已有_dirver，就用这个driver
            self.driver = _driver
        # 如果self.b_url不为空，链接这个url
        if self.b_url != "":
            self.driver.get(self.b_url)
        # 缓冲5s
        self.driver.implicitly_wait(5)
        # 窗口最大化
        self.driver.maximize_window()
    # 创建find方法，参数是by和定位
    def find(self,by,locator):
        # 调用find_element方法，将返回值返回
        return self.driver.find_element(by,locator)