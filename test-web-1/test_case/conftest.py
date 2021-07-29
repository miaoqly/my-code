# File ：conftest.py
# Author ：miao
import pytest
from page.main import Main
# 创建fixture装饰器
@pytest.fixture()
# 获取Main类的实例化方法
def get_main():
    # 实例化Main类
    main = Main()
    # 返回实例化结果
    return main