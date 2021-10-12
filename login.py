import requests
import re
from config import config

class Login:
    def __init__(self):
        self.url = 'https://id.sspu.edu.cn/cas/login'
        self.user = config.get('account', 'sspu_user')
        self.pwd = config.get('account', 'sspu_pwd')
        self.user_agent = config.get('config', 'browse_user_agent')
        self.req_session = requests.Session()
        self.headers = {'user-agent': self.user_agent}
        req = self.req_session.get(self.url)
        self.lt = re.findall(r'name="lt" value="(.*?)"', req.text)[0]
        self.data = {
            'username': self.user,
            'password': self.pwd,
            # imageCodeName:,
            'errors': 0,
            'lt': self.lt,
            '_eventId': 'submit'
        }
        print(self.data)

    def login(self):
        print("正在登录...")
        self.post_url()
        if self.success():
            print("登录成功")
        else:
            print("登录失败")

    def post_url(self):
        self.login_log = self.req_session.post(url=self.url, headers=self.headers, data=self.data)
        # print(self.login_log.text)

    def success(self):
        is_success = re.search('success', self.login_log.text)
        if is_success:
            return 1
        else:
            return 0


login = Login()
login.login()
