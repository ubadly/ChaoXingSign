import requests
import config
from message import Email, Server
from parsel import Selector
import datetime


class ChaoXing:
    def __init__(self):
        self.__username = config.USERNAME
        self.__password = config.PASSWORD
        self.__cookies = {}
        self.login_status = 0
        self.headers = {
            "Host": "mobilelearn.chaoxing.com",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-site",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 Edg/80.0.361.57",
        }
        self.successs = []
        self.error = []
        print('欢迎使用学习通自动签到')

    def login(self):
        '''登录并获取cookie'''
        login_url = "http://passport2.chaoxing.com/api/login"
        params = {
            'name': self.__username,
            'pwd': self.__password,
            'schoolid': '',
            'verify': 0
        }
        try:
            res = requests.get(login_url, params=params, timeout=3)
            if res.json().get('result'):
                # 将获取到的cookie绑定到对象
                self.__cookies = res.cookies.get_dict()
                # 更新登录状态
                self.login_status = 1
                return True
            else:
                print(res.json().get("errorMsg"))
        except Exception as e:
            print("登录失败，错误原因：", e)
            return None

    def sendMsg(self):
        '''
        :param code: 1为成功，0为失败
        :return:
        '''
        message_type = config.MESSAGE_TYPE
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        title = "学习通签到结果"
        sign_time = "签到时间：%s" % now_time
        sucess = f"成功数量：{len(self.successs)}，详情：{','.join(self.successs)}"
        faild = f"失败数量：{len(self.error)}，详情：{','.join(self.error)}"
        content = '\n'.join([sucess, faild, sign_time])
        if message_type == 1:
            m = Email(title=title, content=content)
            m.send(config.RECIVER_EMAILL)

        elif message_type == 2:
            '''此处为server酱部分发送代码'''
            s = Server(config.SERVER_KEY)
            s.send(title, content)
        elif message_type == 3:
            '''此处为mail以及server都发送代码'''
            self.sendForMail(title, content)
            self.sendForServer(title, content)
        else:
            '''此处啥也不干'''
            pass

    def sendForMail(self, title, content):
        '''邮件发送'''
        m = Email(title=title, content=content)
        m.send(config.RECIVER_EMAILL)

    def sendForServer(self, title, content):
        '''Server发送'''
        m = Server(config.SERVER_KEY)
        m.send(title, content.replace('\n', '\n\n'))

    def sign(self):
        if not self.login_status:
            print('没有登录，请先登录！')
            return
        courses = config.COURSE_ID
        school_id = config.SCHOOL_ID
        for course in courses:
            courseId = course['courseId']
            jclassId = course['classId']
            sign_url = "https://mobilelearn.chaoxing.com/widget/pcpick/stu/index?courseId=%s&jclassId=%s" % (
                courseId, jclassId)
            try:
                response = requests.get(sign_url, headers=self.headers, cookies=self.__cookies)
                selector = Selector(response.text)
                ids = selector.css(".wid1100  > div:nth-child(2) .Mct::attr(onclick)").re("\d{6,10}")
                for _id in ids:
                    active_url = 'https://mobilelearn.chaoxing.com/widget/sign/pcStuSignController/preSign?activeId=%s&classId=%s&fid=%s&courseId=%s' % (
                        _id, jclassId, school_id, courseId)
                    try:
                        res = requests.get(active_url, headers=self.headers, cookies=self.__cookies)

                        selector = Selector(res.text)
                        success = selector.css('.qd_Success .greenColor::text').get()
                        if success == '签到成功':
                            print(courseId, "签到成功")
                            self.successs.append(courseId)
                        else:
                            print(courseId, "签到失败")
                            self.error.append(courseId)
                    except Exception as e:
                        print(e)
                        print(courseId, "签到失败")
                        self.error.append(courseId)
            except Exception as e:
                print(e)
                print(courseId, "签到失败")
                self.error.append(courseId)
