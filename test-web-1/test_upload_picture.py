# File ：test_upload_picture.py
# Author ：miao
from time import sleep

from base import Base


class TestUploadPicture(Base):
    def test_uploadpicture(self):
        # 链接网址
        self.driver.get("https://image.baidu.com")
        # 等待3s
        sleep(3)
        # 识别上传图片按钮并点击
        self.driver.find_element_by_css_selector("#sttb>.st_camera_off").click()
        # 识别选择文件按钮并上传
        self.driver.find_element_by_id("uploadImg").send_keys("E:\miaomiaomiao\miao.jpg")
        # 等待5s
        sleep(5)