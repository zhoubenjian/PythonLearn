from time import sleep

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
    
    
def main():
    clock = Clock(23, 20, 30)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
                
        