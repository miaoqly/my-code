import requests

class Base:
    def __init__(self):
        # 获取token
        corpid = "ww4a89e0bb181ec1d5"
        corpsecret = "o_A3sLNTZuicbaviERaxLhh120kPgvYmm91hQ7G_umg"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        # 改写  请求方法用requests  获取json
        # 因为这里是base的构造方法  不能调用下面的普通方法  所以不能用send
        r = requests.get(url).json()
        self.token = r.get('access_token')
        # 声明session
        self.requests_session = requests.Session()
        # 把token放入session中
        self.requests_session.params = {'access_token': self.token}

    def send(self, *args, **kwargs):
        # 改写 requests请求改为session携带token去请求
        r = self.requests_session.request(*args, **kwargs)
        return r.json()