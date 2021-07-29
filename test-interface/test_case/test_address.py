import pytest

from api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()

    @pytest.mark.parametrize("userid,mobile", [("miaomiao123", "13312345677"),
                                               ("miaomiao124", "13312345678"),
                                               ("miaomiao125", "13312345679")])
    def test_add_member(self, userid, mobile):
        name = "today is tuesday 2"
        department = [1]
        # 数据清理
        self.address.delete_member(userid)
        # 创建成员
        r = self.address.add_member(userid=userid, name=name, mobile=mobile, department=department)
        # 断言
        assert r.get("errcode") == 0
        # 查询结果
        r = self.address.get_member(userid=userid)
        # 断言
        # 用get("name","userid 添加失败")可以追加一个参数
        # 当name不存在时会取出"userid 添加失败"
        # 如果用r["name"]没取到name会报错
        assert r.get("name", "userid 添加失败") == name
