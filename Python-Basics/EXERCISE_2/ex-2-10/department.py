from employee import Employee

class Department:
    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees if employees is not None else []

    def add_employee(self, employee):
        """Adds an employee to the department."""
        self.employees.append(employee)

    def list_employees(self):
        """Returns a list of employees in the department."""
        return [f"{emp.name} ({emp.position})" for emp in self.employees]
