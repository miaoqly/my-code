# File ：main.py
from mycode.black import BasePage
from mycode.black.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self.driver)