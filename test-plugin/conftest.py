# File ：conftest.py
import pytest
import yaml

# # items就是要遍历的所有的测试用例
# def pytest_collection_modifyitems(session, config, items:list):
#     for item in items:
#         # item.name用例的名字    item.nodeid用例的路径    把名字和路径改成中文编码    decode是解码
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
#         # 如果测试用例的名字里有login  就加入login标签
#         if 'login' in item.nodeid:
#             item.add_marker(pytest.mark.login)
#     items.reverse()

# 添加命令行参数   参数是Parser类的实例
def pytest_addoption(parser):
    # getgroup定义group（分组）的option（选择）  参数是分组的名字
    mygroup = parser.getgroup("miao")
    # addoption添加组里的参数
    mygroup.addoption("--env",          # 注册一个命令行选项
                      default = 'tests', # 参数默认值
                      dest = 'env',     # 存储的变量
                      help = 'set your run env' # 帮助提示 参数的描述信息
                      )

# 通过fixture接收命令行参数
@pytest.fixture(scope='session')
def cmdoption(request):
    env = request.config.getoption("--env",default='tests')
    if env == 'tests':
        print("测试环境")
        # 指定路径
        datapath = "datas/tests/datas.yaml"
    elif env == 'dev':
        print("开发环境")
        # 指定路径
        datapath = "datas/dev/datas.yaml"
    # 读取配置文件
    with open(datapath) as f:
        datas = yaml.safe_load(f)
    # 返回值追加datas
    return env,datas
