# File ：tag.py
import json
import requests

# 底层封装类
class Tag:
    # 创建构造方法
    def __init__(self):
        # 初始化变量token
        self.token = ""

    # 获取token方法
    def get_token(self):
        # 获取token需要的第一个参数，企业id
        corpid = "ww4a89e0bb181ec1d5"
        # 获取token需要的第二个参数，凭证密钥
        corpsecret = "AQYLnYWJ3l1TnG1ZaQFU1QdithHgzf-Oe98oB6dH3Gg"
        # 获取企业标签库测试用例
        # 获取token的响应放入变量r中
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",
                         params={'corpid': corpid, 'corpsecret': corpsecret}
                         )
        # 拿到json串中的access_token的值，存入初始化过的变量token，这样方法中不需要返回token
        self.token = r.json()['access_token']

    # 获取标签列表方法
    def get_tag_list(self):
        # 获取标签请求结果放入变量r中
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            # 请求体用json格式
            json={
                "tag_id": [],
                "group_id": []
            },
            # 传入token，删除地址中的“?access_token=ACCESS_TOKEN”
            params={'access_token': self.token}
        )
        # 返回请求响应
        return r

    # 添加标签方法，参数为标签组名和标签名
    def add_tag(self,tags,group_name = None):
        print(f"要添加的标签是{tags}")
        if group_name is None :
            json_data = {
                'group_name': "临时组",
                'tag': tags
            }
        elif tags is None:
            print("标签名不能为空")
            return False
        else:
            json_data = {
                # 设置标签组名
                'group_name': group_name,
                # 设置标签名
                'tag': tags
            }
        # 添加标签请求结果放入变量r中
        r = requests.post(
            # 链接地址
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            # 传入token
            params={'access_token': self.token},
            # 请求体用json
            json = json_data
        )
        # 将响应json格式化，间隔为2，并打印
        print(json.dumps(r.json(), indent=2))
        if r.json()['errcode'] == 40071:
            print("标签名已存在")
            return False
        elif r.json()['errcode'] == 40058:
            print("标签名或标签组名过长")
            return False
        elif r.json()['errcode'] == 41018:
            print("标签名不能为空")
        else:
            print("添加标签成功")
            print(tags)
            r = []
            for i in tags:
                r.append(i.get('name'))
            result = self.change_name_to_id(r)
            return self.check_tag_id_exist(result)

    # 标签名转换为标签id方法
    def change_name_to_id(self,tag_name):
        r = self.get_tag_list()
        if isinstance(tag_name,list):
            result = []
            for g in r.json()['tag_group']:
                for h in g['tag']:
                    for t in tag_name:
                        if t == h['name']:
                            result.append(h['id'])
            print(f"标签名转换为id的结果是：{result}")
            return result
        else:
            for g in r.json()['tag_group']:
                # 处理当一个group_id中id数量大于1的情况
                if len(g['tag'])>1:
                    for t in g['tag']:
                        print(t)
                        if tag_name == t['name']:
                            print(f"传入的name是{tag_name}")
                            print(f"切换成id是{t.get('id')}")
                            return t.get("id")
                # 处理当一个group_id只有一个id的情况
                else:
                    if tag_name == g['tag'][0]['name']:
                        print("--------------------")
                        print(f"传入的name是{tag_name}")
                        print(f"切换成id是{g['tag'][0]['id']}")
                        return g['tag'][0].get('id')

    # 标签组名转换为标签组id方法
    def change_group_name_to_group_id(self, group_name):
        r = self.get_tag_list()
        if isinstance(group_name,list):
            result = []
            for g in r.json()['tag_group']:
                for n in group_name:
                    if n == g['group_name']:
                        result.append(g['group_id'])
            return result
        else:
            for g in r.json()['tag_group']:
                if group_name == g['group_name']:
                    return g['group_id']

    # 删除标签方法，参数为：标签name，返回删除的标签id
    def delete_tag(self,tag_name):
        print(f"要删除的标签是:{tag_name}")
        tag_id = self.change_name_to_id(tag_name)
        if tag_id is None:
            print(f"要删除的标签“{tag_name}”不存在")
        else:
            print(f"要删除的tag_id:{tag_id}")
            if isinstance(tag_id,list):
                result = []
                for i in tag_id:
                    # 添加标签请求结果放入变量r中
                    requests.post(
                        # 链接地址
                        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                        # 传入token
                        params={'access_token': self.token},
                        # 请求体用json
                        json={
                            # 传入标签id
                             "tag_id": i
                        }
                    )
                    result.append(i)
                print("删除标签成功")
                return result
            else:
                # 添加标签请求结果放入变量r中
                requests.post(
                    # 链接地址
                    "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                    # 传入token
                    params={'access_token': self.token},
                    # 请求体用json
                    json={
                        # 传入标签id
                        "tag_id": tag_id
                    }
                )
                print("删除标签成功")
                return tag_id

    # 删除标签组方法，参数为：标签组name，返回删除的标签组id
    def delete_group(self, group_name):
        group_id = self.change_group_name_to_group_id(group_name)
        if group_id is None:
            print(f"要删除的标签组“{group_name}”不存在")
        else:
            print(f"要删除的group_id:{group_id}")
            if isinstance(group_id,list):
                result = []
                for g in group_id:
                    # 添加标签请求结果放入变量r中
                    requests.post(
                        # 链接地址
                        "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                        # 传入token
                        params={'access_token': self.token},
                        # 请求体用json
                        json={
                            # 传入标签id
                            "group_id": g
                        }
                    )
                    result.append(g)
                return result
            else:
                # 添加标签请求结果放入变量r中
                requests.post(
                    # 链接地址
                    "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
                    # 传入token
                    params={'access_token': self.token},
                    # 请求体用json
                    json={
                        # 传入标签id
                        "group_id": group_id
                    }
                )
                print("删除标签组成功")
                return group_id

    # 确认标签id是否不存在方法，存在返回True，不存在返回False
    def check_tag_id_exist(self,tag_id):
        if tag_id == []:
            print("标签不存在，无需断言")
            return False
        elif tag_id == "":
            print("标签不存在，无需断言")
            return False
        elif tag_id is None:
            print("标签不存在，无需断言")
            return False
        else:
            # 获取标签列表
            r = self.get_tag_list()
            tag_ids = []
            print(f"check中tag_id：{r.json()['tag_group']}")
            for g in r.json()['tag_group']:
                for t in g['tag']:
                    tag_ids.append(t['id'])
            print(f"tag_id：{tag_id}")
            print(f"tap_ids:{tag_ids}")
            for i in tag_id:
                if i in tag_ids:
                    return True
                else:
                    return False
    # 确认标签组id是否不存在方法，如果不存在，返回True
    def check_group_id_exist(self,group_id):
        if group_id == []:
            print("标签组不存在，无需断言")
        elif group_id == "":
            print("标签组不存在，无需断言")
        elif group_id is None:
            print("标签组不存在，无需断言")
        else:
            # 获取标签列表
            r = self.get_tag_list()
            group_ids = []
            print(f"check中tag_group：{r.json()['tag_group']}")
            for g in r.json()['tag_group']:
                    group_ids.append(g['group_id'])
            print(f"group_id：{group_id}")
            print(f"group_ids:{group_ids}")
            for i in group_id:
                if i in group_ids:
                    return True
                else:
                    return False

    # 清除所有标签组方法，不需要参数，调用后清除所有标签
    def delete_all_group(self):
        # 获取标签列表
        r = self.get_tag_list()
        if r.json()['tag_group'] == []:
            print("没有要删除的标签")
        else:
            group_names = []
            for g in r.json()['tag_group']:
                group_names.append(g['group_name'])
                self.delete_group(group_names)
            result = r.json()['errmsg']
            if result == 'ok':
                print("所有标签删除成功")
                return True
            else:
                print("删除失败")

    # 编辑标签方法
    def edit_tap(self,old_id,new_name):
        print(f"要编辑的标签是{old_id}")
        if isinstance(old_id,str):
            r = requests.post(
                "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
                params={'access_token': self.token},
                json = {
                    "id" : old_id,
                    "name" : new_name
                }
            )
        else:
            print("一次只对一个标签进行修改")
            return False
        # 将响应json格式化，间隔为2，并打印
        print(json.dumps(r.json(), indent=2))
        if r.json()['errcode'] == 40071:
            print("新标签名或组名已存在")
            return False
        elif r.json()['errcode'] == 40058:
            print("新标签名或组名过长")
            return False
        elif r.json()['errcode'] == 41018:
            print("新标签名或组名不能为空")
        elif r.json()['errcode'] == 41018:
            print("旧id不能为空")
        elif r.json()['errcode'] == 41018:
            print("旧id不存在")
        else:
            print("编辑标签成功")
            result = self.change_name_to_id(new_name)
            return self.check_tag_id_exist(result)
