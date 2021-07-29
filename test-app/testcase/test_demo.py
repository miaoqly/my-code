# File ：test_demo.py
from time import sleep
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        # 不清空本地缓存启动，避免聊天记录等数据清除
        caps["noReset"] = "true"
        # 设置页面等待时间为0s，不等渲染那么久，只要进入页面就认为是空闲状态
        # 如果担心页面加载不完成，可以设置为2s、10s
        caps["settings[waitForIdleTimeout]"] = 0

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(7)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        el1 = self.driver.find_element_by_id("com.tencent.wework:id/igk")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/gy9")
        el2.send_keys("刘迎")
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]")
        el3.click()
        el4 = self.driver.find_element_by_id("com.tencent.wework:id/ev3")
        el4.send_keys("喵喵喵")
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/euz")
        el5.click()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        # 滑动查找
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        ele = self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/pu").text
        assert ele == "外出打卡成功"

    def test_add_member(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/cth").click()
        ele_name = self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'姓名')]/../android.widget.EditText")
        ele_name.send_keys("喵喵喵")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        gender = '女'
        if gender == '女':
            self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()
        else:
            self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/fwi").send_keys("136666666666")
        self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/aj_").click()
        toast = self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.Toast']").text
        print(f"提示是：{toast}")
        assert toast == "添加成功"