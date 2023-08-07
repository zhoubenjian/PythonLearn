class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    # 访问器 - getter方法
    @property
    def name(self):
        return self._name
    
    # 访问器 - getter方法
    @property
    def age(self):
        return self._age
        
    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age
        
        
    def play(self):
        if self._age < 18:
            print('%s在玩捉迷藏.' % self._name)
        else:
            print('%s在斗地主.' % self._name)
            
            
def main1():
    person = Person('Jack', 17)
    person.play()
    person.age = 22
    person.play()
    # person.name = 'Mike'    # can't set attribute 'name'
    
    
    
from math import sqrt

class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a
    
    def perimeter(self):
        return self._a + self._b + self._c
    
    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * half * (half - self._b) * half * (half - self._c))
    
def main2():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(f'周长：{t.perimeter()}')
        print(f'面积：{t.area()}')
    else:
        print('无法构成三角形.')
    
    
    
# 继承和多态
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        self._grade = grade
        
    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))
        
        
class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
        
    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))

def main3():
    s = Student('Michael', 15, '大学')
    s.study('math')       
    s.play() 
    
    t = Teacher('Steve', 38, '校长')
    t.teach('Python从入门到精通.')
    t.play()



# 抽象类
from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname
        
    # 抽象方法
    @abstractmethod
    def make_voice(self):
        pass
    

class Dog(Pet):
    def make_voice(self):
        return '%s：汪汪汪' % self._nickname
        
        
class Cat(Pet):
    def make_voice(self):
        return '%s：喵喵喵' % self._nickname
    
def main4():
    pets = [Dog('旺财'), Cat('海胆'), Dog('阿黄')]
    for pet in pets:
        print(pet.make_voice())
    
    
        
    
if __name__ == '__main__':
    main1()
    main2()
    main3()
    main4()
    