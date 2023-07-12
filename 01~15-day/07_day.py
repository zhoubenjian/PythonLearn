s1 = 'hello world!'
s2 = "hello world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello
world!
"""
print(s1, s2, s3, end='')

print()

# '\'转义字符
s4 = '\'hello,world!\''
s5 = '\n\\hello, world!\\\n'
print(s4, s5, end='')

print()

s1 = 'hello ' * 3
print(s1)           # hello hello hello
s2 = 'world'
s1 += s2
print(s1)           # hello hello hello world
print('ll' in s1)   # True
print('good' in s1) # False

print()

str1 = 'abc123456'
print(str1[2])      # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str1[2:5])    # c12
print(str1[2:])     # c123456
print(str1[-3:-1])  # 45
print(str1[2::2])   # c246
print(str1[::2])    # ac246
print(str1[::-1])   # 654321cba
print(str1[::-2])   # 642ca
print(str1[-3::-1]) # 4321cba
print(str1[1::-3])  # b
print(str1[-1::-3]) # 63c

print()

str1 = 'hello, world!'
print(len(str1))                # 13
print(str1.capitalize())        # Hello, world!
print(str1.title())             # Hello, World!
print(str1.upper())             # HELLO, WORLD!
print(str1.find('or'))          # 8
print(str1.find('shit'))        # -1（未找到）
print(str1.startswith('he'))    # True
print(str1.startswith('al'))    # False
print(str1.center(50, '*'))     # 指定宽度居中，*补齐
print(str1.rjust(50, ' '))      # 制定宽度居右， 补齐
print(str1.ljust(50, '-'))      # 制定宽度居左，-补齐

str2 = 'abc123456'
print(str2.isdigit())           # False 是否数字字符串
print(str2.isalpha())           # False 是否字母字符串
print(str2.isalnum())           # True  是否数字字母字符串

str3 = '  jackfrued@126.com '
print(str3.strip())             # jackfrued@126.com 去除空格

print()

a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')

print()

# list
list1 = [2, 3, 4, 5, 7, 11, 13, 17, 19]
print(list1)                # [2, 3, 4, 5, 7, 11, 13, 17, 19]
list2 = ['Scofield']        
print(list2 * 3)            # ['Scofield', 'Scofield', 'Scofield']
print(len(list1))           # 9
print(list1[0])             # 2
print(list1[-1])            # 19
# print(list1[9])             # IndexError: list index out of range
list1[0] = 1                # 赋值
print(list1)                # [1, 3, 4, 5, 7, 11, 13, 17, 19]

# 下标遍历
for i in range(len(list1)):
    print(list1[i])    

# for...in 遍历
for index in list1:
    print(index)
    
# enumerate: 遍历索引和值
for index, value in enumerate(list1):
    print(index, value)