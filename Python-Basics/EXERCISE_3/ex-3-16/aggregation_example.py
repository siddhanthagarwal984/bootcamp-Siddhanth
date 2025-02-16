class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"{self.name} ({self.position})"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def __str__(self):
        return f"Department: {self.name}, Employees: {[str(emp) for emp in self.employees]}"

# Creating employees
emp1 = Employee("Alice", "Engineer")
emp2 = Employee("Bob", "Manager")

# Creating a department and adding employees (Aggregation)
dept = Department("IT")
dept.add_employee(emp1)
dept.add_employee(emp2)

print(dept)
