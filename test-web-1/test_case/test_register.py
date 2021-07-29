# File ：test_register.py
# Author ：miao
# 创建测试类TestRegister
class TestRegister:
    # 创建测试方法test_register，将conftest.py的feature方法名当作参数传入测试方法中
    def test_register(self,get_main):
        # 从主页跳转到登录页面再跳转到注册页面，输入企业名称和管理员姓名，并获取手机号元素的name属性的值并断言
        assert "registerTel" == get_main.goto_login().goto_register().register()