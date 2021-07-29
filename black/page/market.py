# File ：market.py
from mycode.black import BasePage
from mycode.black.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self.driver)