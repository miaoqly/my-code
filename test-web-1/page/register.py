# File ：register.py
# Author ：miao
from time import sleep
from selenium.webdriver.common.by import By
from page.base import Base
# 注册页面的Page Object，继承Base类
class Register(Base):
    # 定义注册方法
    def register(self):
        sleep(5)
        # 定位企业名称输入框并输入：miao
        self.find(By.ID,"corp_name").send_keys("miao")
        sleep(5)
        # 定位管理员姓名输入框并输入：miaomiao
        self.find(By.ID,"manager_name").send_keys("miaomiao")
        # 定位管理员手机号并获取它的name属性并返回
        return self.driver.find_element(By.ID,"register_tel").get_attribute("name")
