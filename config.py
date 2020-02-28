# 学习通账户
USERNAME = ""
# 学习通密码
PASSWORD = ""

# 学校ID
SCHOOL_ID = 9859

# 需要签到的课程信息,按照我的格式来
COURSE_ID = [
    {
        "courseId": "",
        'classId': ""
    },
]

# 签到结果通知类型
# 0为不发送，1为邮件方式，2为server酱方式，3为同时使用1和2发送信息
MESSAGE_TYPE = 0

# 邮箱配置信息，MESSAGE_TYPE设置为1时生效
# 邮箱的key，需要用QQ邮箱，或者自行修改源码
EMAIL_KEY = ""
# 邮箱发送者
SEND_EMAIL = ""
# 邮箱接收者
RECIVER_EMAILL = ""

# 接收消息的server酱的key,MESSAGE_TYPE设置为2时生效
# server酱官网：http://sc.ftqq.com/3.version
SERVER_KEY = ""
