# 找出所有水仙花数
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == (low ** 3 + mid ** 3 + high ** 3):
        print(num)
        
print()

# 正整数的反转
num = int(input('请输入数字：'))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

print()

# 《百钱百鸡》问题
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if x * 5 + y * 3 + z/3 == 100:
            print('公鸡:%d, 母鸡:%d, 小鸡:%d' % (x, y, z))