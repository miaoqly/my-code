import allure
# 关联网址
@allure.link("http://www.baidu.com",name="链接")
def test_with_link():
        print("这是一条加了链接的测试")
        pass
# 关联测试用例地址
TEST_CASE_LINK = 'https://github.com/qameta/allure-integrations/issues/8#issuecomment-268313637'
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_testcase_link():
        print("这是一条测试用例的链接，链接到你的测试用例页面")
        pass
# 关联bug,地址只能在运行的时候给，参数是bugid和说明
@allure.issue('140','这是一个issue')
def test_with_issue_link():
        pass