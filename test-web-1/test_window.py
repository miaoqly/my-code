# File ：test_window.py
# Author ：miao
from time import sleep

from base import Base


class TestWindow(Base):
    def test_window(self):
        # 链接网址
        self.driver.get("https://www.baidu.com")
        # 定位登录按钮并点击
        self.driver.find_element_by_link_text("登录").click()
        # 定位立即注册按钮并点击
        self.driver.find_element_by_link_text("立即注册").click()
        # 获取当前窗口句柄
        win1 = self.driver.current_window_handle
        # 打印当前窗口句柄
        print(win1)
        # 获取所有窗口句柄
        win = self.driver.window_handles
        # 打印所有窗口句柄
        print(win)
        # 切换到第二个窗口
        self.driver.switch_to_window(win[1])
        # 等待3s
        sleep(3)
        # 定位用户名输入框并输入用户名
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("miao")
        # 定位手机号输入框并输入手机号
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("133333333333")
        # 等待3s
        sleep(3)
        # 切换到第一个窗口
        self.driver.switch_to_window(win[0])
        # 等待3s
        sleep(3)
        # 定位用户名登录按钮并点击
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        # 等待3s
        sleep(3)
        # 定位手机号输入框并输入手机号
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("13333333333")
        # 定位密码输入框并输入密码
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("233")
        # 定位登录按钮并点击
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        # 等待3s
        sleep(3)
