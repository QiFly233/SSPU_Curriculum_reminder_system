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
            self.login_eams()
            self.course_num()
            self.course_table()
        else:
            print("登录失败")
        self.logout()

    def post_url(self):
        self.login_log = self.req_session.post(url=self.url, headers=self.headers, data=self.data)
        # print(self.login_log.text)

    def success(self):
        is_success = re.search('success', self.login_log.text)
        if is_success:
            return 1
        else:
            return 0

    def login_eams(self):
        print('登录教务系统...')
        url = 'https://jx.sspu.edu.cn/eams/login.action'
        self.req_session.get(url)

    def course_num(self):
        # self.login_eams()
        url = 'https://jx.sspu.edu.cn/eams/dataQuery.action'
        log = self.req_session.post(url=url, data={'dataType': 'semesterCalendar'})
        num = re.findall('id:(.*?),schoolYear:"(.*?)",name:"(.*?)"', log.text)
        self.current_semester_num = num[len(num)-1][0]
        print(self.current_semester_num)
        self.semester_num = {}
        for i in range(len(num)):
            self.semester_num[num[i][1]+num[i][2]+'学期'] = num[i][0]

    def course_table(self):
        url = 'https://jx.sspu.edu.cn/eams/courseTableForStd.action'
        log = self.req_session.get(url)
        ids = re.findall('bg.form.addInput\\(form,"ids","(.*)"\\);', log.text)[0]
        print(ids)
        data = {
            'ignoreHead': '1',
            'setting.kind': 'std',
            'startWeek': '1',
            'semester.id': str(self.current_semester_num),
            'ids': ids,
        }
        print(data)
        url = 'https://jx.sspu.edu.cn/eams/courseTableForStd!courseTable.action'
        log = self.req_session.post(url=url, data=data, headers=self.headers)
        print(log.text)

    def logout(self):
        self.req_session.cookies.clear()


login = Login()
login.login()
