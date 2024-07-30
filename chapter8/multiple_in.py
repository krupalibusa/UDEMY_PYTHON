class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Dancer():
    def __init__(self,dance_style):
        self.style = dance_style

class Student(Person,Dancer):
    def __init__(self, name, age,dance_style):
        Person.__init__(self,name, age)
        Dancer.__init__(self,dance_style)

obj1 = Student("KRUPALI",29,"Hiphop")
print(obj1.name)
print(obj1.age)
print(obj1.style)