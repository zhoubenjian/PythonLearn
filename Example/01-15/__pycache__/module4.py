# 变量的作用域
def foo():
    # 局部变量（local variable）
    b = 'hello'
    
    # Python中可以在函数内部再定义函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)
        
    bar()
    
if __name__ == '__main__':
    # 全局变量（global variable）
    a = 100
    foo()