class Employee:
    def __init__(self, name, emp_id, position):
        self.name = name
        self.emp_id = emp_id
        self.position = position

    def __str__(self):
        return f"{self.name} ({self.position})"
