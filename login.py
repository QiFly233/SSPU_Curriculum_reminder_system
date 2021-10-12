import requests
import re
from config import config

class Login:
    def __init__(self):
        self.url = 'https://id.sspu.edu.cn/cas/login'
        self.user = config.get('account', 'sspu_user')
        self.pwd = config.get('account', 'sspu_pwd')
        self.req = requests.get(self.url)
        self.lt = re.findall(r'name="lt" value="(.*?)"', self.req.text)[0]
        print(self.user)
        print(self.pwd)
        print(self.lt)

    def post_url(self):
        data = {
            'username': self.user,
            'password': self.pwd,
            # imageCodeName:,
            'errors': 0,
            'lt': self.lt,
            '_eventId': 'submit'
        }



login = Login()
