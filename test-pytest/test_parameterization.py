import pytest
import yaml
# 测试用例参数化
class TestData:
    # 利用字符串作为变量实现参数化，参数化的值用列表嵌套元祖实现
    @pytest.mark.parametrize("a,b",[(10,20),(30,40),(50,60)])
    def test_string(self,a,b):
        print(a+b)
# 数据量少的时候参数化的变量用列表或元祖代替，参数化的值用列表嵌套元祖实现，注意列表和元祖的区别
    @pytest.mark.parametrize(["a","b"],[(10,20),(30,40),(50,60)])
    def test_list(self,a,b):
        print(a*b)
    @pytest.mark.parametrize(("a","b"),[(10,20),(30,40),(50,60)])
    def test_tuple(self,a,b):
        print(b-a)
# 数据量大时参数化的值用yaml文件代替
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./test_param.yaml")))
    def test_yaml(self,a,b):
        print(b/a)

# 设置一个参数env，导入yaml配置文件，打印出配置文件的所有内容，注意yaml配置文件写法
    @pytest.mark.parametrize("env",yaml.safe_load(open('./test_env.yaml')))
    def test_env(self,env):
        if "test" in env:
            print("这是测试环境，IP是",env['test'])
        if "dev" in env:
            print("这是开发环境，IP是",env['dev'])