class Employee:
    def __init__(self, name, age, employee_id):
        self.name = name
        self.age = age
        self.employee_id = employee_id
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}"
    
class Manager(Employee):
    def __init__(self, name, age, employee_id, department, team_size):
        super().__init__(name, age, employee_id)
        self.department = department
        self.team_size = team_size

    def display_info(self):
        employee_info = super().display_info()
        return f"{employee_info}, Department: {self.department}, Team Size: {self.team_size}"
    
class TeamLead(Employee):
    def __init__(self, name, age, employee_id, project_assignment, num_team_members):
        super().__init__(name, age, employee_id)
        self.project_assignment = project_assignment
        self.num_team_members = num_team_members

    def display_info(self):
        employee_info = super().display_info()
        return f"{employee_info}, Project Assignment: {self.project_assignment}, Number of Team Members: {self.num_team_members}"

class SoftwareEngineer(Employee):
    def __init__(self, name, age, employee_id, programming_languages, project_involvement):
        super().__init__(name, age, employee_id)
        self.programming_languages = programming_languages
        self.project_involvement = project_involvement

    def display_info(self):
        employee_info = super().display_info()
        return f"{employee_info}, Programming Languages: {', '.join(self.programming_languages)}, Project Involvement: {self.project_involvement}"

manager = Manager("John Doe", 40, "M001", "Engineering", 10)
team_lead = TeamLead("Jane Smith", 35, "TL001", "Project A", 5)
software_engineer = SoftwareEngineer("Alice Johnson", 30, "SE001", ["Python", "Java"], "Project B")

print("Manager Details:")
print(manager.display_info())

print("\nTeam Lead Details:")
print(team_lead.display_info())

print("\nSoftware Engineer Details:")
print(software_engineer.display_info())