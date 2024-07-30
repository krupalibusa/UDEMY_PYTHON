class Staff:
    def __init__(self,name , age , contact_no):
        self.name = name
        self.age = age
        self.contact_no = contact_no

    def display_info(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("contact no: ", self.contact_no)

class Faculty(Staff):
    def __init__(self,name , age,contact_no,dep ,degree ,rank):
        super().__init__(name,age, contact_no)
        self.degree = degree
        self.rank = rank
        self.dep=dep

    def display_info(self):
        print_staff = super().display_info()
        print(print_staff)
        print("Department: ", self.dep)
        print("degree: ", self.degree)
        print("Rank  : ", self.rank)
        

class AssiProfessor(Faculty):
    def __init__(self,name , age , contact_no,dep ,degree ,rank,publication):
        super().__init__(name , age,contact_no,dep ,degree ,rank)
        self.publication = publication
        
    def display_info(self):
        print_faculty = super().display_info()
        print(print_faculty)
        print("publication : ", self.publication)
        

emp1 = AssiProfessor("Mayur", 30 , "123344","IT","PHD",3,"TATA")
emp1.display_info()
