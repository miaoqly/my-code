# File ：test_miao.py
import pytest

@pytest.mark.parametrize("name",["大大","喵喵","欢欢"])
def test_miao(name):
    print(name)

def test_login():
    print("login")

def test_login_fail():
    print("login")
    assert False

def test_search():
    print("search")

def test_env(cmdoption):
    # print(cmdoption)
    # 接收数据
    env,datas = cmdoption
    # 读取数据
    host = datas['env']['host']
    port = datas['env']['port']
    # 拼接url 注意强转字符串
    url = str(host) + ":" + str(port)
    print(url)