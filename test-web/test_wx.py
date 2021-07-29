# File ：test_wx.py
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX:
    def setup(self):
        # 设置复用浏览器端口，获取cookies后不再使用
        # option = Options()
        # option.debugger_address = "localhost:9222"
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wx(self):
        # 获取cookies，得到cookies后不再使用
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # cookies = self.driver.get_cookies()
        # print(cookies)

        # cookies存入小型数据库，存入后不再使用
        # cookies = [{'domain': '.qq.com', 'expiry': 1613440586, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688849965564416'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': '5Vu5KWZU4-PpM3MWaQgI3huTrZJ2DuBezuMKS81sgFWtyMafsI-PikpWAAREefLp_0VY-lgmqhT1a8NOOgQ2sSdLAc3JriOArTTt5CzFDhWMqLAq-fgrRWHmdZ2-CpRsFwE3cCp2koyG0u7_3xd-_XD-irjsKBOLFOa5CPvr9RjLLLU9UMVl0sickF9xhMq91aaZ6snqyJW09Sa-TurTBm_FNxWviyp1AGRDERBjWKRvhJOvWShsJjfu4YMZ3ePbQhGXnoC9TCXwuHMHBQ5B6Q'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688849965564416'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324997379850'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a2232036'}, {'domain': 'work.weixin.qq.com', 'expiry': 1613471719, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8p5tpp2'}, {'domain': '.qq.com', 'expiry': 1613526926, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.299311476.1613440188'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '18053274612983745'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'FOl0GlapBqaRnRHJ8CNb00uaW2XFBetv_OW6lQzF9NguMhkRQIc0o7BIpmC-ln95'}, {'domain': '.qq.com', 'expiry': 1676512526, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1422996111.1613440188'}, {'domain': '.work.weixin.qq.com', 'expiry': 1644976183, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1616032539, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        # db = shelve.open('cookies')
        # db['cookie'] = cookies
        # db.close()

        # 打开小型数据库文件存入db变量中
        db = shelve.open('cookies')
        # 取出变量中的key值放入变量cookies中
        cookies = db['cookie']
        # 关闭小型数据库
        db.close()
        # 访问企业微信登录首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 循环读取cookies
        for cookie in cookies:
            # 判断key值如果是过期时间戳
            if 'expiry' in cookie:
                # 删除对应的key和value
                cookie.pop('expiry')
            # 读取的cookie通过add_cookie方法传入地址
            self.driver.add_cookie(cookie)
        # 读取cookies后刷新页面
        self.driver.refresh()
        sleep(3)
        # 获取添加成员按钮元素并点击
        self.driver.find_element(By.CSS_SELECTOR,'.js_service_list>a:nth-child(1)').click()
        sleep(3)
        # 获取姓名输入框元素并输入‘miao‘
        self.driver.find_element(By.ID,'username').send_keys('miao')
        # 获取帐号输入框元素并输入’miao‘
        self.driver.find_element(By.ID,'memberAdd_acctid').send_keys('miao')
        # 获取手机输入框元素并输入‘13555555555’
        self.driver.find_element(By.ID,'memberAdd_phone').send_keys('13555555555')
        # 获取保存按钮元素并点击
        self.driver.find_elements(By.CSS_SELECTOR,'.js_btn_save')[0].click()
        sleep(3)
        # 获取通讯录姓名为miao的元素的text属性存入变量result中
        result = self.driver.find_elements(By.CSS_SELECTOR,'#member_list td:nth-child(2)')[1].text
        # 断言获取到的text属性值result是‘miao’
        assert result == 'miao'
        sleep(3)

