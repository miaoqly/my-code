import allure
import pytest
from selenium import webdriver
import time
# 链接到测试用例管理地址，这里用github代替
@allure.testcase("http://www.github.com")
# 功能点前加个feature或者story
@allure.feature("百度搜索")
# 参数化测试数据
@pytest.mark.parametrize('test_data1',['allure','pytest','unittest'])
def test_steps_demo(test_data1):
    # 每一个关键步骤前加个step对每一个步骤进行说明
    with allure.step("打开百度网页"):
        # 配置了环境变量后不需要传值，但如果是先编辑代码后配置环境变量需要重启pycharm
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        # 打开浏览器后将窗口最大化
        driver.maximize_window()
    # 这里的搜索词是用的参数化传过来的
    with allure.step(f"输入搜索词：{test_data1}"):
        driver.find_element_by_id("kw").send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)
    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        # 将保存的图片插入到测试步骤中
        allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)
        allure.attach('<head></head><body>首页</body>','Attach with HTML type',attachment_type=allure.attachment_type.HTML)
    with allure.step("退出浏览器"):
        driver.quit()