# File ：app.py
from appium import webdriver
from mycode.black import BasePage
from mycode.black import Main


class App(BasePage):
    package = "com.xueqiu.android"
    activity = "view.WelcomeActivityAlias"
    def start(self):
        if self.driver is None:
            caps = {
                "platformName":"android",
                "deviceName":"127.0.0.1:7555",
                "appPackage":self.package,
                "appActivity":self.activity,
                "autoGrantPermissions":True,
                "unicodeKeyBoard":True,
                "resetKeyBoard":True
            }
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.start_activity(self.package,self.activity)
        return self
    def main(self):
        return Main(self.driver)