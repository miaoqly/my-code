# File ：test_tag.py
import allure
import pytest
import yaml
from tag import Tag

# 读取yaml文件方法
def load_data(path):
    with open(path, encoding='utf-8') as f:
        return yaml.safe_load(f)

# 创建测试企业标签类
@allure.feature("客户标签模块")
class TestTag:
    # 把可以重复使用的实例化tag放入setup中
    def setup(self):
        # 实例化tag类
        self.tag = Tag()
        # 获取token
        self.tag.get_token()
        # 清除数据
        # self.tag.delete_all_group()

    # 测试获取标签方法
    @allure.story("获取标签")
    def test_get_tag(self):
        # 获取标签列表
        r = self.tag.get_tag_list()
        # 断言状态码是200
        assert r.status_code == 200
        # 断言errcode是0
        assert r.json()['errcode'] == 0

    # 测试添加标签方法
    @allure.story("添加标签")
    @pytest.mark.parametrize("tag_names,group_name",
                             load_data("test_tag.yaml")["test_add_tag"])
    def test_add_tag(self,tag_names,group_name):
        # 调用添加标签方法
        result = self.tag.add_tag(tag_names, group_name)
        assert result

    # 测试添加标签方法，只传标签名
    @allure.story("通过标签名添加标签")
    @pytest.mark.parametrize("tag_names",
                             load_data("test_tag.yaml")["test_add_only_tag"])
    def test_add_only_tag(self,tag_names):
        # 调用添加标签方法
        result = self.tag.add_tag(tag_names)
        assert result

    # 测试添加重复标签方法
    @allure.story("添加重复标签")
    @pytest.mark.parametrize("tag_names,group_name",
                             load_data("test_tag.yaml")["test_re_add_tag"])
    def test_re_add_tag(self,tag_names,group_name):
        # 调用添加标签方法
        result = self.tag.add_tag(tag_names, group_name)
        assert result

    # 测试添加标签失败方法，只添加标签组名
    @allure.story("只添加标签组名")
    @pytest.mark.parametrize("tag_names,tag_group",
                             load_data("test_tag.yaml")["test_add_tag_fail_only_group"])
    def test_add_tag_fail_only_group(self,tag_names,tag_group):
        # 调用添加标签方法
        result = self.tag.add_tag(tag_names,tag_group)
        assert result

    # 测试添加标签失败方法，标签组和标签名称最多只有有30个字符
    @allure.story("添加标签失败")
    @pytest.mark.parametrize("group_name,tag_names",
                             load_data("test_tag.yaml")["test_add_tag_fail"])
    def test_add_tag_fail(self,group_name,tag_names):
        # 调用添加标签方法
        result = self.tag.add_tag(group_name,tag_names)
        assert result

    # 测试删除标签方法
    @allure.story("删除标签")
    @pytest.mark.parametrize("tag_name",
                             load_data("test_tag.yaml")["test_delete_tag"])
    def test_delete_tag(self,tag_name):
        # 创建要删除的文件
        self.tag.add_tag([{'name':'tag_dmiao_0218'}],'group_dmiao_0218')
        # 调用删除标签方法,返回id
        tag_id = self.tag.delete_tag(tag_name)
        # 查找是否删除成功
        check = self.tag.check_tag_id_exist(tag_id)
        # 断言结果是删除成功
        assert check == False

    # 测试删除标签组方法
    @allure.story("删除标签组")
    @pytest.mark.parametrize("group_name",
                             load_data("test_tag.yaml")["test_delete_group"])
    def test_delete_group(self,group_name):
        # 创建要删除的文件
        self.tag.add_tag([{'name':'tag_delete_miao_0218'}],'group_delete_miao_0218')
        # 调用删除标签组方法
        group_id = self.tag.delete_group(group_name)
        # 调用查找id是否存在方法，如果删除成功，返回True
        check = self.tag.check_group_id_exist(group_id)
        # 断言结果是删除成功
        assert check == False

    # 测试删除标签不存在方法
    @allure.story("删除标签不存在")
    @pytest.mark.parametrize("tag_name",
                             load_data("test_tag.yaml")["test_delete_tag"])
    def test_delete_tag(self,tag_name):
        # 调用删除标签方法,返回id
        tag_id = self.tag.delete_tag(tag_name)
        # 查找是否删除成功
        check = self.tag.check_tag_id_exist(tag_id)
        # 断言结果是删除成功
        assert check

    # 测试删除不存在标签组方法
    @allure.story("删除标签组不存在")
    @pytest.mark.parametrize("group_name",
                             load_data("test_tag.yaml")["test_delete_group"])
    def test_delete_group(self,group_name):
        # 调用删除标签组方法
        group_id = self.tag.delete_group(group_name)
        # 调用查找id是否存在方法，如果删除成功，返回True
        check = self.tag.check_group_id_exist(group_id)
        # 断言结果是删除成功
        assert check == False

    # 测试删除多个标签方法
    @allure.story("删除多个标签")
    @pytest.mark.parametrize("tag_name",
                             load_data("test_tag.yaml")["test_deletes_tag"])
    def test_deletes_tag(self,tag_name):
        # 创建要删除的文件
        self.tag.add_tag([{'name':'tag_delete1_miao_0218'},{'name':'tag_delete2_miao_0218'}],'group_delete_miao_0218')
        # 调用删除标签方法,返回id
        tag_id = self.tag.delete_tag(tag_name)
        # 查找是否删除成功
        check = self.tag.check_tag_id_exist(tag_id)
        # 断言结果是删除成功
        assert check == False

    # 测试删除多个标签组方法
    @allure.story("删除多个标组签")
    @pytest.mark.parametrize("group_name",
                             load_data("test_tag.yaml")["test_deletes_group"])
    def test_deletes_group(self,group_name):
        # 创建要删除的文件
        self.tag.add_tag([{'name':'tag_delete1_miao_0218'},{'name':'tag_delete2_miao_0218'}],'group_delete_miao_0218')
        self.tag.add_tag([{'name':'tag_delete11_miao_0218'}],'group_delete1_miao_0218')
        # 调用删除标签方法,返回id
        group_id = self.tag.delete_group(group_name)
        # 查找是否删除成功
        check = self.tag.check_group_id_exist(group_id)
        # 断言结果是删除成功
        assert check == False

    # 清除所有数据
    def test_delete_all(self):
        result = self.tag.delete_all_group()
        assert result