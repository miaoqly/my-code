# File ：market_page.py
from page.basepage import BasePage
from page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.steps("../page/data/market_page.yaml","goto_search")
        return SearchPage(self.driver)
