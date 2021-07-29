# File ：search.py
from mycode.black import BasePage


class Search(BasePage):
    def search(self,value):
        self.params["value"] = value
        self.steps("../page/search.yaml")