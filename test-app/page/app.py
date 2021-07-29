# File ：app.py
from appium import webdriver
from page.basepage import BasePage
from page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": "true",
                "ensureWebviewsHavePages": True,
                # 设置页面等待空闲状态时间为0s
                "settings[waitForIdleTimeout]": 0
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            # 自动拉取Capabilities配置信息启动，不需要任何初始化操作
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()
        return self

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
