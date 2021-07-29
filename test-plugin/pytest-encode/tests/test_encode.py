# File ：test_encode.py
import pytest


@pytest.mark.parametrize("name",["大大","喵喵","欢欢"])
def test_miao(name):
    print(name)