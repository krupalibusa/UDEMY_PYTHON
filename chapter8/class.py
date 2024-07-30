class Employee:
    emp_id  = 0
    emp_name = ""
    emp_salary = 0.0

    def __init__(self,id , name , salary):
        self.emp_id = id
        self.emp_name = name 
        self.emp_salary = salary 

    def print_data(self):
        print("Id of employee is: ",self.emp_id)
        print("Name of employee is: ",self.emp_name)
        print("Salary of employee is: ",self.emp_salary)

emp1 = Employee(1,"KRUPALI",10000)
emp2 = Employee(2,'Rani',60000)
print('Employee 1 info')
emp1.print_data()
emp2.print_data()
