import os
import time
import random

# 练习1：在屏幕上显示跑马灯文字。
def runHourse():
    content = '上海自来水来自海上'
    while True:
        os.system('cls')  # 清空控制台
        print(content)
        time.sleep(0.2)   # 休眠200ms
        content = content[1:] + content[0]
        
if __name__ == '__main__':
    runHourse()
        
    
# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
def captcha(code_length = 6):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for _ in range(0, code_length):
        index = random.randint(0, len(all_chars) - 1)
        code += all_chars[index]
    return code

if __name__ == '__main__':
    captcha()
    
    
# 练习3：设计一个函数返回给定文件名的后缀名。
def get_suffix(filename, has_dot = False):
    pos = filename.rfind('.')               # 最后一个'.'的索引（没有：-1）
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''
    
    
# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for i in range(2, len(x)):
        if x[i] > m1:
            m2 = m1
            m1 = x[i]
        elif x[i] > m2:
            m2 = x[i]
    return m1, m2
      
            
# 练习5：计算指定的年月日是这一年的第几天。
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, day):
    day_num = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], 
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ]
    total = 0
    for i in range(month - 1):
        total += day_num[is_leap_year(year)][i]
    return (total + day)

    