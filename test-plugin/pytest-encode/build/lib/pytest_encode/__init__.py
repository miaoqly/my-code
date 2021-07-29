# File ：__init__.py.py
from typing import List

# items就是要遍历的所有的测试用例
def pytest_collection_modifyitems(session, config, items:List):
    for item in items:
        # item.name用例的名字    item.nodeid用例的路径    把名字和路径改成中文编码    decode是解码
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    items.reverse()