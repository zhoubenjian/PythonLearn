# 用户身份验证
username = input('请输入用户名：\n')
password = input('请输入密码：\n')

if username == 'admin' and password == '123456':
    print('身份验证成功...')
else:
    print('身份验证失败...')
    
print()

# 分段函数求值
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x > -1:
    y = 5 * x + 3
else:
    y = x + 2
print('f(%.2f) = %.2f' % (x, y))

print()

# 英制单位英寸与公制单位厘米互换
value = float(input('请输入长度：'))
str = input('请输入单位：')
if str == 'in' or str == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.45))
elif str == 'cm' or str == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.45))
else:
    print('未知单位')
    
print()

# 百分制成绩转换为等级制成绩。
score = float(input('请输入成绩：'))
if score > 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score > 70:
    grade = 'C'
elif score > 60:
    grade = 'D'
else:
    grade = 'E'
print(grade)

print()

# 输入三条边长，如果能构成三角形就计算周长和面积
a = float(input('请输入边长a：'))
b = float(input('请输入边长b：'))
c = float(input('请输入边长c：'))
if (a + b > c) and (a + c > b) and (b + c > a):
    p = (a + b + c) / 2
    print('三角形周长：%f' % (a + b + c))
    print(f'三角形面积：{(p * (p - a) * (p - b) * (p - c)) ** 0.5}')
else:
    print('不能构成三角形')
    
