# File ：test_timedate.py
# Author ：miao
from time import sleep

from base import Base


class TestTimeDate(Base):
    def test_timedate(self):
        # 链接网址
        self.driver.get("https://www.12306.cn")
        # 移除时间控件readonly属性的js语句存在变量中
        # date_js1 = "document.getElementById('train_date').removeAttribute('readonly')"
        # 给时间空间赋值的js语句存在变量中
        # date_js2 = "document.getElementById('train_date').value='2021-02-07'"
        # 执行移除readonly属性js语句
        self.driver.execute_script("document.getElementById('train_date').removeAttribute('readonly')")
        # 等待5s
        sleep(5)
        # 执行赋值js语句
        self.driver.execute_script("document.getElementById('train_date').value='2021-02-07'")
        # 等待5s
        sleep(5)