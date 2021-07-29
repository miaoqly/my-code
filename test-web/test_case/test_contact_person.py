# File ：test_contact_person.py
from page.index_page import IndexPage

# 创建测试联系人类
class TestContactPerson:
    def setup(self):
        # 实例化首页page
        self.index = IndexPage()

    def teardown(self):
        pass

    # 创建添加联系人方法，断言方式通过左侧栏搜索
    def test_contact_person(self):
        # 创建调用添加联系人方法所需要的三个变量并赋值
        name = "dadademiaomiao"
        acctid = "dadademiaomiao"
        phone = "13888888888"
        # 调用通过首页page添加联系人方page并将结果page放入变量add_page中
        add_page = self.index.goto_add_member()
        # 调用添加联系人方法并传参
        add_page.add_member(name,acctid,phone)
        # 调用通过左侧栏搜索联系人姓名方式获取联系人姓名方法并将返回的姓名放入result参数中
        result = add_page.get_member(name)
        # 断言调用方法返回的姓名与设置传参变量name的值相等
        assert result == name

    def test_turn_page(self):
        # 创建调用添加联系人方法所需要的三个变量并赋值
        name = "miaomiaodedada"
        acctid = "miaomiaodedada"
        phone = "13999999999"
        # 调用通过首页page添加联系人方page并将结果page放入变量add_page中
        add_page = self.index.goto_add_member()
        # 调用添加联系人方法并传参
        add_page.add_member(name,acctid,phone)
        # 调用通过右侧栏翻页查找方式获取联系人姓名方法并将返回的True or False放入result参数中
        result = add_page.turn_page(name)
        # 由于返回值本身就是True or False，直接断言即可
        assert result