from employee import Employee

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = {}

    def add_employee(self, employee):
        self.employees[employee.emp_id] = employee

    def remove_employee(self, emp_id):
        """Removes an employee from the department."""
        if emp_id in self.employees:
            del self.employees[emp_id]

    def total_salary(self):
        """Calculates total salary of all employees."""
        return sum(emp.salary for emp in self.employees.values())
