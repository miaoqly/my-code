# File ：test_frame.py
# Author ：miao
from base import Base

class TestFrame(Base):
    def test_frame(self):
        # 链接网址
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换进子节点
        self.driver.switch_to.frame("iframeResult")
        # 打印子节点中按钮的文本
        print(self.driver.find_element_by_id("draggable").text)
        # 切换回默认节点
        # self.driver.switch_to_default_content()
        # 还可以切换回父节点
        self.driver.switch_to.parent_frame()
        # 打印默认节点中按钮的文本
        print(self.driver.find_element_by_id("submitBTN").text)

