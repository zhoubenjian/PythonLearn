def foo():
    pass
    
def bar():
    pass

def alt():
    pass
    
# 引入module3，默认 不会 执行
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
    print('call alt()')
    alt()

# 引入module3，默认执行
print('call foo()')
foo()
print('call bar()')
bar()
print('call alt()')
alt()