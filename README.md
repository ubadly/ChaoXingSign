# 超星学习通签到
 超星签到

推荐`python3.6+`版本

首次使用请安装需要的依赖库：

```shell
pip3 install -r requirements.txt
```

配置文件在<u>config.py</u> ，账号仅支持手机号方式登录

SCHOOL_ID为每个学校对应的ID

CLASSID 和 COURSE_ID里面的参数为每个班课的信息，请参考：

![](https://yangbaimg.syoogame.com/tmp/000/00/00/00/5e589b3c429c8.jpg)

MESSAGE_TYPE签到的结果通知方式分为邮件和server酱的方式

默认不推送，设置邮件的方式请设置相关配置，本意是设置为服务型代码，所有设置的对于个人使用较为麻烦，推荐使用server酱的方式推送

代码执行入口：

```shell
python3 start.py
```

这是第一个版本，有问题请提交

推荐放到服务器上设置cron来定时执行

设置教程：[https://blog.csdn.net/lzghxjt/article/details/80375626](https://blog.csdn.net/lzghxjt/article/details/80375626)