import allure
def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)
def test_attach_html():
    allure.attach("<body>这是一段htmlbody</body>","html测试块",attachment_type=allure.attachment_type.HTML)
def test_attach_picture():
    # 不是纯文本要加file方法
    allure.attach.file("E:\miaomiaomiao\picture\miaomiao.jpg",name="这是一个图片",attachment_type=allure.attachment_type.JPG)