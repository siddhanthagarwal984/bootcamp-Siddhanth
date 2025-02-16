class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

class Project:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.employees = []

    def assign_employee(self, employee):
        self.employees.append(employee)

class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def department_summary(self):
        return {dept.name: len(dept.employees) for dept in self.departments}

# Example usage
company = Company("TechCorp")
it_department = Department("IT")
company.add_department(it_department)

employee1 = Employee("Alice", "Engineer")
it_department.add_employee(employee1)

project1 = Project("AI Research", it_department)
project1.assign_employee(employee1)

print(company.department_summary())
