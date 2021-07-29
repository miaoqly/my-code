# File ：main_page.py
from page.basepage import BasePage
from page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        self.steps("../page/data/main_page.yaml","goto_market_page")
        return MarketPage(self.driver)
    def goto_mine_page(self):
        self.steps("../page/data/main_page.yaml","goto_mine_page")
        # return MinetPage(self.driver)
