from employee import Employee

class Manager(Employee):
    def __init__(self, name, emp_id, position, subordinates=None):
        super().__init__(name, emp_id, position)
        self.subordinates = subordinates if subordinates is not None else []

    def add_subordinate(self, employee):
        """Adds an employee to the manager's list of subordinates."""
        self.subordinates.append(employee)

    def list_subordinates(self):
        """Returns a list of subordinate names."""
        return [emp.name for emp in self.subordinates]
