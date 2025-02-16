class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self._position = position  # Private variable
        self._salary = salary

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        if not new_position:
            raise ValueError("Position cannot be empty")
        self._position = new_position

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
emp = Employee("Bob", "Manager", 60000)
print(emp)

# Updating position
emp.position = "Senior Manager"
print(emp)
