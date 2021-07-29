# File ：__init__.py.py
import logging
from typing import List

# 添加日志
logging.basicConfig(level=logging.INFO,
                             # 日志格式
                             # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
                             format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(me',
                             # 打印日志的时间
                             datefmt='%a, %d %b %Y %H:%M:%S',
                             # 日志文件存放的目录（目录必须存在）及日志文件名
                             filename='report.log',
                             # 打开日志文件的方式
                             filemode='w'
                             )
logger = logging.getLogger(__name__)




# items就是要遍历的所有的测试用例
def pytest_collection_modifyitems(session, config, items:List):
    for item in items:
        # item.name用例的名字    item.nodeid用例的路径    把名字和路径改成中文编码    decode是解码
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
    items.reverse()