"""
函数递归调用 - 函数直接或者间接的调用了自身
1. 收敛条件
2. 递归公式

n! = n * (n-1)!
f(n) = f(n-1) + f(n-2)
1 1 2 3 5 8 13 21 34 55 ...
"""


# 阶乘
def fac(num):
    # assert 断言
    assert num >= 0, 'num不能小于0'
    if num in (0, 1):
        return 1
    return num * fac(num - 1)


# 斐波那契数组
def fib1(num):
    a, b = 1, 1
    for _ in range(num - 1):
        a, b = b, a + b
    return a


def fib2(num):
    '''生成器'''
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a
        


"""主函数"""
def main():
    print(fac(5))
    print(fib1(5))
    
    print('------')
    
    generator_object = fib2(8)
    for i in generator_object:
        print(i)
    


if __name__ == '__main__':
    main()