class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} ({self.position})"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def __str__(self):
        return f"Department: {self.name}, Employees: {[str(emp) for emp in self.employees]}"

class Project:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def __str__(self):
        return f"Project: {self.name}, Department: {self.department.name}, Employees: {[str(emp) for emp in self.employees]}"

# Creating department, employees, and project
dept = Department("IT")
emp1 = Employee("Alice", "Engineer")
emp2 = Employee("Bob", "Manager")
dept.add_employee(emp1)
dept.add_employee(emp2)

project = Project("AI Development", dept)
project.add_employee(emp1)

print(dept)
print(project)
