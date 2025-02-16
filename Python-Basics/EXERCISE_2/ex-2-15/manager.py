from employee import Employee

class Manager(Employee):
    def __init__(self, name, emp_id, position, salary, subordinates=None):
        super().__init__(name, emp_id, position, salary)
        self.subordinates = subordinates if subordinates is not None else []

    def __str__(self):
        return f"Manager {self.name}, Position: {self.position}, Managing: {len(self.subordinates)} employees"

    def __repr__(self):
        return f"Manager({self.name!r}, {self.emp_id!r}, {self.position!r}, {self.salary!r}, {self.subordinates!r})"
