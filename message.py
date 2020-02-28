import smtplib
from email.mime.text import MIMEText
from email.header import Header
import requests
import config


class Email:
    msg_from = config.SEND_EMAIL
    passwd = config.EMAIL_KEY

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.msg = MIMEText(self.content)
        self.msg['Subject'] = Header(self.title, charset='utf-8')
        self.msg['From'] = Header(self.msg_from, charset='utf-8')

    def send(self, receivers):
        '''邮件发送'''
        '''
        receivers: 需要发送的地址
        '''
        if not receivers:
            print('发送失败，请在config配置文件中设置RECIVER_EMAILL参数')
            return
        self.msg['To'] = receivers
        try:
            # 通过ssl方式发送，服务器地址，端口
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            # 登录到邮箱
            s.login(self.msg_from, self.passwd)
            # 发送邮件：发送方，收件方，要发送的消息
            s.sendmail(self.msg_from, receivers, self.msg.as_string())
            print('邮件发送成功！')
        except Exception as e:
            print('邮件发送失败！', e)


class Server:
    def __init__(self, key):
        self.key = key

    def send(self, title, content):
        try:
            url = "https://sc.ftqq.com/%s.send" % self.key
            params = {
                'text': title,
                'desp': content
            }
            requests.get(url=url, params=params, timeout=3)
            print('Server酱微信推送成功！')
        except Exception as e:
            print('Server酱微信推送失败！', e)
