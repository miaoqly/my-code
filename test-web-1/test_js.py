# File ：test_js.py
# Author ：miao
from time import sleep

from base import Base


class TestJS(Base):
    def test_js(self):
        # 链接网址
        self.driver.get("https://www.baidu.com")
        # js方式定位输入框
        ele1 = self.driver.execute_script("return document.getElementById('kw')")
        # 向输入框中输入搜索关键字
        ele1.send_keys("selenium测试")
        # js方式定位搜索按钮
        ele2 = self.driver.execute_script("return document.getElementById('su')")
        # 点击搜索按钮
        ele2.click()
        # 等待3s
        sleep(3)
        # js方式滑动到底部
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        # 等待3s
        sleep(3)
        # 获取下一页按钮并点击
        self.driver.find_element_by_css_selector("#page>.page-inner>:nth-last-child(1)").click()
        # 等待3s
        sleep(3)
        # 通过js方法循环打印title和性能数据
        # for case in[
        #     'return document.title',
        #     'return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(case))
        # 也可以将js多条语句合并，“;”分隔
        print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)'))