# File ：base_page.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 基类，用来完成初始化操作，存放最基本的方法
class BasePage:
    # 声明url变量为空
    _base_url = ""

    # 创建构造方法，设置driver初始值为None
    def __init__(self,_driver : WebDriver = None):
        # 判断如果没有driver
        if _driver == None:
            # 使用复用9222端口浏览器
            option = Options()
            option.debugger_address = "localhost:9222"
            # 实例化webdriver，创建driver
            self.driver = webdriver.Chrome(options=option)
            # 缓冲5s
            self.driver.implicitly_wait(5)
        # 如果有driver，复用driver
        else:
            self.driver = _driver

        # 判断如果有url，就链接这个url
        if self._base_url != "":
            self.driver.get(self._base_url)

    # 封装查找单个元素方法，参数为定位方法和定位值
    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    # 封装查找多个元素方法，参数为定位方法和定位值
    def finds(self,by,locator):
        return self.driver.find_elements(by,locator)

    # 封装隐式等待可被点击方法，参数为元祖属性的locator，超时时间默认10s
    def wait_for_click(self,locator,timeout = 10):
        WebDriverWait(self.driver,timeout).until(expected_conditions.element_to_be_clickable(locator))