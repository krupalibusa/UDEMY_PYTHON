class BaseClass:
    __name = None
    def __init__(self,name):
        self.__name = name

    def __print_data(self):
        print(self.__name)
    
obj1 = BaseClass("John")
obj1.__print_data()
