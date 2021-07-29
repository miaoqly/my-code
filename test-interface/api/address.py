from api.base import Base

class Address(Base):
    # **kwargs代表可以添加任意参数（一个*代表不限数量的列表参数 两个*代表不限数量的字典参数）
    # 数据类型不严格遵守也不会报错  只是提示类型
    def add_member(self, userid: str, name: str, mobile: str, department: list, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        # 对body字典中追加新的参数
        body.update(kwargs)
        # 改写  请求方法用send 直接返回请求结果
        return self.send("post",url, json=body)

    def get_member(self, userid: str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        # 改写  请求方法用send 直接返回请求结果
        return self.send("get",url)

    def update_member(self, userid: str, name: str, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {
            "userid": userid,
            "name": name
        }
        body.update(kwargs)
        # 改写  请求方法用send 直接返回请求结果
        return self.send("post",url, json=body)

    def delete_member(self, userid: str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        # 改写  请求方法用send 直接返回请求结果
        return self.send("get",url)
