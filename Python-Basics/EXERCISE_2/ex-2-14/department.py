from employee import Employee

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = {}

    def add_employee(self, employee):
        self.employees[employee.emp_id] = employee

    def __str__(self):
        return f"Department: {self.name}, Employees: {len(self.employees)}"

    def __repr__(self):
        return f"Department({self.name!r}, {self.employees!r})"
