class Employee:
    def __init__(self, name, emp_id, position, salary):
        self.name = name
        self.emp_id = emp_id
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"Employee {self.name}, Position: {self.position}, Salary: ${self.salary}"

    def __repr__(self):
        return f"Employee({self.name!r}, {self.emp_id!r}, {self.position!r}, {self.salary!r})"
