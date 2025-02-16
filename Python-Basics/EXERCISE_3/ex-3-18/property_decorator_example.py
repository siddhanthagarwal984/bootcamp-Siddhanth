class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self._salary = salary  # Private variable

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):
        if amount < 30000:
            raise ValueError("Salary must be at least 30,000")
        self._salary = amount

    def __str__(self):
        return f"{self.name} ({self.position}), Salary: ${self.salary}"

# Example usage
emp = Employee("Alice", "Engineer", 50000)
print(emp)

# Trying to set a low salary
try:
    emp.salary = 20000
except ValueError as e:
    print(e)
