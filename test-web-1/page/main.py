# File ：main.py
# Author ：miao
from time import sleep
from selenium.webdriver.common.by import By
from login import Login
from page.base import Base
from page.register import Register
# 主页的Page Object，继承Base类
class Main(Base):
    # 重写父类属性并修改值
    b_url = "https://work.weixin.qq.com/"
    # 跳转到注册页面方法
    def goto_register(self):
        sleep(5)
        # 定位立即注册按钮并点击
        self.find(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
        # 返回立即注册Page Object，参数给一个已有的driver
        return Register(self.driver)
    # 跳转到登录页面方法
    def goto_login(self):
        sleep(5)
        # 定位企业登录按钮并点击
        self.find(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        # 返回企业登录Page Object，参数给一个已有的driver
        return Login(self.driver)