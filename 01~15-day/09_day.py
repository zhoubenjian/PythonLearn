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
    
    
        
    
if __name__ == '__main__':
    main1()
    main2()
    