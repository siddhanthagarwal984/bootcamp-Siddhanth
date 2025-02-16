from employee import Employee

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = {}  # Dictionary with emp_id as key

    def add_employee(self, employee):
        """Adds an employee to the department."""
        self.employees[employee.emp_id] = employee

    def get_employee(self, emp_id):
        """Retrieves an employee by ID."""
        return self.employees.get(emp_id, None)
