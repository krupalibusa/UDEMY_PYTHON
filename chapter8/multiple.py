class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Dancer:
   def __init__(self,dance_style):
        self.dance_style = dance_style

class Student(Person,Dancer):
    def __init__(self, name, age,dance_style):
        Person.__init__(self,name, age)
        Dancer.__init__(self,dance_style)

std1 = Student("KRUPALI",29,"Hiphop")
print(std1.dance_style)
print(std1.name)