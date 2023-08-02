import DayTrain08 as dt08

class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def study(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))
        
    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能看《熊出没》' % (self.name))
        else:
            print('%s可以看岛国动作大电影' % (self.name))
            

# 私有属性           
class Test():
    def __init__(self, foo):
        # __代表私有（private）
        self.__foo = foo
        
    def _bar(self):
        print(self.__foo)
        print('_bar')
    
            
            
def main1():
    # 实例化
    student1 = Student('大耳朵图图', 6)
    student1.study('八荣八耻')
    student1.watch_movie()
    
    student2 = Student('张无忌', 19)
    student2.study('Python程序设计语言')
    student2.watch_movie()
    
    
# def main2():
#     test = Test('hello')
#     test.__bar()        # 'Test' object has no attribute '__bar'
#     print(test.__foo)   # AttributeError: 'Test' object has no attribute '__foo'
    
    
if __name__ == '__main__':
    main1()
    # main2()
    
    # dt08.main1()
    
    dt08.main2()