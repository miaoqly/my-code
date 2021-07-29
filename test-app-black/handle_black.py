# File ：handle_black.py
# 定义装饰器处理黑名单
import yaml


def handle_black(fun):
    def run(*args, **kwargs):
        # 取fun也就是find方法的参数是(self,locator)，他的第0个参数，就是self
        instance = args[0]
        with open("../black_list.yaml", "r", encoding="utf-8") as f:
            black_list = yaml.safe_load(f).get("black_list")
        # 捕获异常（元素没有找到）
        try:
            # find方法是有return，所以也要加return
            return fun(*args, **kwargs)
        except Exception as e:
            # 遍历黑名单
            for black in black_list:
                # 获取黑名单元素
                eles = instance.driver.find_elements(*black)
                # 如果黑名单元素长度大于0，说明有弹窗
                if len(eles) > 0:
                    # 点掉弹窗
                    eles[0].click()
                    # 这里的参数locator，改成接收任意参数即可
                    # 也可以不用instance.find重新调用查找方法，直接用fun，也就是find方法
                    return fun(*args, **kwargs)
            raise e

    return run
