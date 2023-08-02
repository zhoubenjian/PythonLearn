from time import sleep
from math import sqrt

# 练习1：定义一个类描述数字时钟。
class Clock(object):
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
        
    def run(self):
        self.__second += 1
        if(self.__second == 60):
            self.__second = 0
            self.__minute += 1
            if(self.__minute == 60):
                self.__minute = 0
                self.__hour += 1
                
    def show(self):
        return '%02d:%02d:%02d' % (self.__hour, self.__minute, self.__second)
    
    
def main1():
    clock = Clock(23, 20, 30)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
        
    
# 练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def move_to(self, x, y):
        self.x = x
        self.y = y
        
    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx **2 + dy **2)
    
    # __str__类比Java的toString()
    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))
    

def main2():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    print(p1.distance_to(p2))
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))
    

        
                
        