# 修改全局变量
def foo():
    # 声明a为全局变量
    global a
    a = 200
    print(a)

if __name__ == '__main__':
    a = 100
    foo()
    print(a)