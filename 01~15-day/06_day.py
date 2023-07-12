from random import randint

# # 求阶乘（函数）
# def fac(num):
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     return result

# m = int(input('m='))
# n = int(input('n='))
# print(fac(m) // fac(n) // fac(m -n))

# print()

# # 函数
# def roll_dice(n = 2):
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total

# def add(a = 0, b = 0, c = 0):
#     return a + b + c

# # 如果没有指定参数那么使用默认值摇两颗色子
# print(roll_dice())
# # 摇三颗色子
# print(roll_dice(3))

# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))

# # 传递参数时可以不按照设定的顺序进行传递
# print(add(c = 50, a = 100, b = 200))

# print()

# # 可变参数
# def sum(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total

# print(sum())
# print(sum(1))
# print(sum(1, 2, 3, 4))

# print()

# # 练习1：实现计算求最大公约数
# def gcd(x, y):
#     (x, y) = (y, x) if x > y else (x, y)
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor

# # 练习1：最小公倍数的函数        
# def lcm(x, y):
#     return (x * y) // gcd(x, y)

# print()

# 练习2：实现判断一个数是不是回文数的函数。
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

num = int(input('请输入：'))
print(is_palindrome(num))

print()

# 练习3：实现判断一个数是不是素数的函数
def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    # if...else 写一行
    return True if num !=1 else False

print()


        