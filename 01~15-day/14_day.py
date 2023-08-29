from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    sender = 'xxx.com'
    receivers = ['yyy@qq.com', 'zzz@qq.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('Benjamin', 'utf-8')
    message['To'] = Header('Rain', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.163.com')
    # 请自行修改下面的登录口令
    smtper.login(sender, 'RFTSKJHQHCVUWHKN')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()