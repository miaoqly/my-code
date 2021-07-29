# File ：test_search.py
from mycode.black import App
class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search("阿里巴巴")