# File ：add_member_page.py
from selenium.webdriver.common.by import By
from page.base_page import BasePage

# 创建添加联系人page，继承基类
class AddMemberPage(BasePage):
    # 创建添加联系人方法，参数为姓名、帐号、手机号
    def add_member(self,name,acctid,phone):
        # 查找姓名输入框元素并输如name的值
        self.find(By.ID,"username").send_keys(name)
        # 查找姓名输入框元素并输入参数acctid的值
        self.find(By.ID,"memberAdd_acctid").send_keys(acctid)
        # 查找姓名输入框元素并输入参数phone的值
        self.find(By.ID,"memberAdd_phone").send_keys(phone)
        # 查找保存按钮元素并点击
        self.finds(By.CSS_SELECTOR,".js_btn_save")[0].click()

    # 创建获取联系人是否保存成功方法，这里是通过左侧栏搜索查询像，参数value为传入的name
    def get_member(self,value):
        # 获取搜索框元素按钮元素保存到变量search中
        search = self.find(By.ID,"memberSearchInput")
        # 点击搜索框元素
        search.click()
        # 向搜索框输入参数value的值
        search.send_keys(value)
        # 获取查找结果第一个元素的文本信息存入变量result中
        result = self.finds(By.CSS_SELECTOR,".ww_searchResult_title_peopleName")[0].text
        # 返回查找结果
        return result

    # 创建获取联系人是否保存成功方法，这里是通过右侧列表翻页查找，参数value为传入的name
    def turn_page(self,value):
        # 避免页面加载过慢，对姓名前的勾选框的可点击属性进行显式等待
        self.wait_for_click((By.CSS_SELECTOR,".ww_checkbox"))
        # 设置所有页面姓名的title的列表为空
        titles_total = []
        # 循环读取所有页面数据
        while True:
            # 获取列表中所有姓名属性放入变量elements中
            elements = self.finds(By.CSS_SELECTOR,"#member_list :nth-child(2)")
            # 通过列表推导式遍历elements中所有姓名的title值放入titles变量中
            titles = [element.get_attribute("title") for element in elements]
            # 判断如果找到了传入的姓名在titles中
            if value in titles:
                # 返回True，不再查找后面的页面
                return True
            # 通过extend方法titles的值传入所有页面，因为是在循环中，会将每一页的姓名title追加到titles_total中
            titles_total.extend(titles)
            # 获取当前页数/总页数元素的text属性并放入page变量中，对page变量进行字符串格式强转，便于分割字符串
            page:str = self.find(By.CSS_SELECTOR,".ww_pageNav_info_text").text
            # 通过split方法分割字符串，分割标准是“/”，分割次数为1，将当前页数和总页数分割并存入变量num和total中
            num,total = page.split("/",1)
            # 强转变量num和total的类型为数值型，判断如果当前页数等于总页数，还没有找到元素
            if int(num) == int(total):
                # 返回False
                return False
            # 如果当前页数不等于总页数，点击下一页按钮
            else:
                self.find(By.CSS_SELECTOR,".js_next_page").click()