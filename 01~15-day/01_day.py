# 加减乘除
a = 321
b = 12
print(a + b)    # 333
print(a - b)    # 309
print(a * b)    # 3852
print(a / b)    # 26.75

print()

# 除
print(5 / 2)
# 模
print(5 % 2)
# 整除
print(5 // 3)

print()



# 练习3：输入年份判断是不是闰年。
'''
①能被4整除，且不能被400整除；
或
②能被400整除；
'''
year = int(input('请输入年份：\n'))
is_leap = (year % 4 == 0 and year % 400 != 0) or (year % 400 == 0) 
print('%d年是闰年：%s' % (year, is_leap))