class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    # 访问器 - getter方法
    @property
    def name(self):
        return self.__name
    
    # 访问器 - getter方法
    @property
    def age(self):
        return self.__age
        
    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self.__age = age
        
        
    def play(self):
        if self.__age < 18:
            print('%s在玩捉迷藏.' % self.__name)
        else:
            print('%s在斗地主.' % self.__name)
            
            
def main():
    person = Person('Jack', 17)
    person.play()
    person.age = 22
    person.play()
    # person.name = 'Mike'    # can't set attribute 'name'
    
    
if __name__ == '__main__':
    main()
    