import smtplib
from email.mime.text import MIMEText
from config import config
from courses import courses
from timer import timer

class Email:
    def __init__(self):
        self.sender = config.get('email', 'sender')
        self.receiver = []
        self.receiver.append(config.get('email', 'receiver'))
        self.smtp_host = config.get('email', 'smtp_host')
        self.smtp_pwd = config.get('email', 'smtp_pwd')
        self.name = config.get('email', 'name')

    def message(self):
        msg = courses.handle()
        week = str(timer.get_week())
        today_course = msg[week]
        print(today_course)
        while True:
            next_time = timer.get_next_time()
            for j in range(len(today_course)):
                print(next_time)
                if next_time in today_course[j]:
                    print(today_course[j][next_time])

        self.msg = MIMEText(msg, 'plain', 'utf-8')
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver[0]
        self.msg['subject'] = 'Test'

    def send(self):

        smtp = smtplib.SMTP(self.smtp_host)
        print(smtp)
        smtp.login(self.sender, self.smtp_pwd)
        smtp.sendmail(self.name, self.receiver, self.msg.as_string())
        smtp.quit()
        print("成功")


emails = Email().message()
