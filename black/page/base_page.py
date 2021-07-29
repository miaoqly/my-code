# File ：base_page.py
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    black_list = []
    error_count = 0
    error_max = 10
    params = {}
    def __init__(self,_driver:WebDriver=None):
        self.driver = _driver
    def find(self,by,locator):
        try:
            element = self.driver.find_elements(*by) if isinstance(by,tuple) else self.driver.find_element(by,locator)
            self.error_count = 0
            return element
        except Exception as e:
            self.error_count += 1
            if self.error_count >= self.error_max:
                raise e
            for black in self.black_list:
                elements = self.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by,locator)
            raise e
    def send(self,value,by,locator):
        try:
            self.find(by,locator).send_keys(value)
            self.error_count = 0
        except Exception as e:
            self.error_count +=1
            if self.error_count >= self.error_max:
                raise e
            for black in self.black_list:
                elements = self.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                return self.send(value,by,locator)
            raise e
    def steps(self,path):
        with open(path,encoding="utf-8") as f:
            steps:list[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"],step["locator"])
                    if "action" in step.keys():
                        if "click" == step["action"]:
                            element.click()
                        if "send" == step["action"]:
                            content:str = step["value"]
                            for param in self.params:
                                content = content.replace("{%s}"%param,self.params[param])
                            self.send(content,step["by"],step["locator"])