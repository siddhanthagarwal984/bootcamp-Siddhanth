from employee import Employee

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        """Aggregates an employee (but they can exist independently)."""
        self.employees.append(employee)

    def list_employees(self):
        return ", ".join(str(emp) for emp in self.employees)
