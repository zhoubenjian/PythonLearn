import sys


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
    
print()

list1 = [1, 3, 5, 7, 100]
list1.append(200)
# 指定位置插入(insert)
list1.insert(1, 400)
# 合并
list1.extend([2, 4, 6, 8])
print(list1)            # [1, 400, 3, 5, 7, 100, 200, 2, 4, 6, 8]
print(len(list1))       # 11

# 是否存在
if 3 in list1:
    list1.remove(3)         # 移除元素3
if 250 in list1:
    list1.remove(250)       # 不存在，无法移除
print(list1)

# 删除指定位置元素(pop)
list1.pop(0)
print(list1)                # [400, 5, 7, 100, 200, 2, 4, 6, 8]
list1.pop(len(list1) - 1)  
print(list1)                # [400, 5, 7, 100, 200, 2, 4, 6]    

print()

# list 切片
fruits1 = ['apple', 'banana', 'mango', 'orange'] 
fruits1 += ['pear', 'strawberry', 'watermelon'] 
print(fruits1)              # ['apple', 'banana', 'mango', 'orange', 'pear', 'strawberry', 'watermelon']

fruits2 = fruits1[1:4]
print(fruits2)              # ['banana', 'mango', 'orange']

# 完整复制
fruits3 = fruits1[:]        
print(fruits3)              # ['apple', 'banana', 'mango', 'orange', 'pear', 'strawberry', 'watermelon']

fruits4 = fruits1[-3:-1]
print(fruits4)              # ['pear', 'strawberry']     

# 可以通过反向切片操作来获得倒转后的列表的拷贝 
fruits5 = fruits1[::-1]     
print(fruits5)              # ['watermelon', 'strawberry', 'pear', 'orange', 'mango', 'banana', 'apple']

print()

# list 排序
list1 = ['banana', 'mango', 'apple', 'orange']
# sorted函数返回列表排序后的拷贝不会修改传入的列表
list2 = sorted(list1)
print(list2)                # ['apple', 'banana', 'mango', 'orange']

# 转置
list3 = sorted(list1, reverse=True)
print(list3)                # ['orange', 'mango', 'banana', 'apple']

# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)
print(list4)                # ['mango', 'apple', 'banana', 'orange']

# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)                # ['orange', 'mango', 'banana', 'apple']

print()

# 生成式和生成器

f = [x for x in range(1, 10)]
print(f)                    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

f = [x + y for x in 'abc' for y in '1234']
print(f)                    # ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4']

# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))     # 查看对象占用内存的字节数
# print(f)

# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f))     # 相比生成式生成器不占用存储数据的空间
# print(f)

print()

# 元组

# 定义元组
t = ('Benjamin', 28, True, '江苏南京')
print(t)                    # ('Benjamin', 28, True, '江苏南京')
# 获取元素
print(t[0])                 # Benjamin
print(t[3])                 # 江苏南京

# 遍历
for member in t:
    print(member)
    
# 重新赋值
# t[0] = 'KLOSE'              # TypeError   元组无法单独修改元素       
t = ('KLOSE', 41, False, '德国柏林')
print(t)                    # ('KLOSE', 41, False, '德国柏林')

# 元组转列表
list = list(t)
print(list)                 # ['KLOSE', 41, False, '德国柏林']

# 列表是可以修改它的元素的
list[0] = '李小龙'
list[1] = 25
print(list)                 # ['李小龙', 25, False, '德国柏林']

# 将列表转换成元组
fruits_list = ['apple', 'banana', 'orange', 'watermelon']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)         # ('apple', 'banana', 'orange', 'watermelon')
