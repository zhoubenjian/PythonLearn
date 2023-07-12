from math import sqrt
import random

# 0~9
for i in range(10):
    print(i, end=',')

print()

# 左闭右开
for i in range(1, 10):
    print(i, end=',')

print()

for i in range(1, 12, 2):
    print(i, end=',')
    
print()

sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)

print()

# 猜数字游戏
# random：左闭右闭
answer = random.randint(1, 100)
count = 0
print('已生成一个[1, 100]之间的随机数。')
while True:
    number = int(input('请输入：'))
    count += 1
    if number > answer:
        print('大了')
    elif number < answer:
        print('小了')
    else:
        print('恭喜你，猜对了')
        break    
print('你一共猜了%d次' % count)
if count >= 8:
    print('你的智商堪忧~')
    
print()

# 输出乘法口诀表(九九表)
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d × %d = %d" % (i, j, i * j), end='\t')
    print()

print()

# 输入一个正整数判断它是不是素数
# num = int(input('请输入数字：'))
# end = int(sqrt(num))
# is_prime = True
# for i in range(2, end + 1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d is prime' % num)
# else:
#     print('%d is not prime' % num)
    
print()

# 输入两个正整数计算它们的最大公约数和最小公倍数
x = int(input('请输入x：'))
y = int(input('请输入y：'))
if x > y:
    # 交换x，y的值
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是：%d' % (x, y, factor))
        print('%d和%d的最小公倍数是：%d' % (x, y, x * y // factor))
        break