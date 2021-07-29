# File ：test_xueqiu.py
from page.app import App


class TestMarket:
    def setup(self):
        self.app = App()

    def test_search(self):
        value = "阿里巴巴"
        result = self.app.start().goto_main().goto_market_page(). \
            goto_search().search(value)
        assert result == value

    def test_mine(self):
        self.app.start().goto_main().goto_mine_page()