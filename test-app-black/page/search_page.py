# File ：search_page.py
from page.basepage import BasePage


class SearchPage(BasePage):
    def search(self,value):
        self.params["value"] = value
        result = self.steps("../page/data/search_page.yaml","search")
        return result