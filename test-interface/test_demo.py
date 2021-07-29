# File ：test_demo.py
from time import sleep
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 创建读取yaml文件方法
def load_data(path):
    with open(path,encoding='utf-8') as f:
        return yaml.safe_load(f)
# 创建测试类
class TestData:
    # 设置装饰器，实现测试数据参数化，参数值为：传入方法的变量，读取文件的数据
    @pytest.mark.parametrize('data',load_data('test_data.yaml')['data'])
    def test_data(self,data):
        # 设置循环读取yaml文件，实现测试步骤参数化，读取yaml文件steps列表中数据放入step中
        for step in load_data('test_data.yaml')['steps']:
            # 如果step中key值有webdriver
            if 'webdriver' in step:
                # 如果webdriver中key值有remote-debugging-port
                if 'remote-debugging-port' in step.get('webdriver'):
                    # 创建复用浏览器端口设置为本机的9222
                    option = Options()
                    option.debugger_address = 'localhost:9222'
                    # 取出webdriver中key值为browser的值，并强转为字符串格式再转为小写字母，放入变量browser中
                    browser = str(step.get('webdriver').get('browser')).lower()
                    # 如果chrome等于brower
                    if 'chrome' == browser:
                        # 创建driver，复用9222端口Chrome浏览器
                        self.driver = webdriver.Chrome(options=option)
            # 如果step中key值有get
            if 'get' in step:
                # 取出key值为get的value放入url变量中
                url = step.get('get')
                # 链接url
                self.driver.get(url)
            # 如果step中key值有find_element
            if 'find_element' in step:
                # 如果find_element的类型是列表
                if isinstance(step.get("find_element"),list):
                    # 取列表第一个序列值放入变量by中
                    by = step.get("find_element")[0]
                    # 取列表第二个序列值放入变量locator中
                    locator = step.get("find_element")[1]
                # 如果find_element的类型是字典
                elif isinstance(step.get("find_element"),dict):
                    # 取出字典中key值为by的value放入变量by中
                    by = step.get("find_element")['by']
                    # 取出字典中key值为value的value放入变量locator中
                    locator = step.get("find_element")['value']
                # 调用查找元素方法，参数为by和locator，并将结果放入变量element中
                element = self.driver.find_element(by,locator)
            # 如果step中key值有click
            if 'click' in step:
                # 执行元素点击
                element.click()
            # 如果step中key值有send_keys
            if 'send_keys' in step:
                # 获取key值为send_keys的value放入value变量中，并强转为字符串格式
                value:str = step.get("send_keys")
                # 对value做字符串替换，替换为方法中传入data参数，并重新给value赋值
                value = value.replace("${data}",data)
                # 元素输入value
                element.send_keys(value)
        sleep(3)
        self.driver.quit()