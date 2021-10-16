import smtplib
from email.mime.text import MIMEText
from config import config


class Email:
    def __init__(self):
        self.sender = config.get('email', 'sender')
        self.receiver = []
        self.receiver.append(config.get('email', 'receiver'))
        self.smtp_host = config.get('email', 'smtp_host')
        self.smtp_pwd = config.get('email', 'smtp_pwd')
        self.name = config.get('email', 'name')

    def message(self):
        msg = 'test'
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


emails = Email()
