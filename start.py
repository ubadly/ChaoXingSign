from Chaoxing import ChaoXing


def start():
    cx = ChaoXing()
    status = cx.login()
    if status:
        cx.sign()
        cx.sendMsg()
    else:
        print('登录失败！')
if __name__ == '__main__':
    start()