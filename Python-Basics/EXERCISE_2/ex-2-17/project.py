from department import Department
from employee import Employee

class Project:
    def __init__(self, name, department):
        self.name = name
        self.department = department  # Association with Department
        self.employees = []  # Aggregation of Employees

    def assign_employee(self, employee):
        self.employees.append(employee)

    def list_employees(self):
        return ", ".join(str(emp) for emp in self.employees)
