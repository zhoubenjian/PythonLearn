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

