# File ：index_page.py
from selenium.webdriver.common.by import By
from page.add_member_page import AddMemberPage
from page.base_page import BasePage

# 创建首页page，继承基类
class IndexPage(BasePage):
    # 重写父类变量_base_url，设置链接网址
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 创建去到添加联系人page
    def goto_add_member(self):
        # 查找添加联系人按钮元素并点击
        self.find(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        # 返回去到添加联系人page，参数给driver，复用driver
        return AddMemberPage(self.driver)