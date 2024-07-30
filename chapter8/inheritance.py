class Person:
    name = ""
    contact_no = ""
    def __init__(self,n1,cn1):
        self.name = n1
        self.contact_no = cn1
    def print_info(self):
        print("Name is: ",self.name)
        print("Contact No: ",self.contact_no)

class Student(Person):
    grade = ""
    percentage = 60.0
    def __init__(self, n1, cn1,gr):
        super().__init__(n1, cn1)
        self.grade= gr

    def percetage_update(self,per):
        self.percentage = self.percentage + per


std1 = Student("KRUPALI","1234345","10th")
std1.percetage_update(20)
std1.print_info()
print(std1.percentage)