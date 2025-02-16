class Employee:
    def __init__(self, name, emp_id, position, salary):
        self.name = name
        self.emp_id = emp_id
        self._position = position  # Private attribute
        self._salary = salary  # Private attribute

    @property
    def position(self):
        """Getter for position"""
        return self._position

    @position.setter
    def position(self, new_position):
        """Setter for position with validation"""
        allowed_positions = ["Engineer", "Manager", "Designer", "HR"]
        if new_position in allowed_positions:
            self._position = new_position
        else:
            raise ValueError(f"Invalid position! Allowed: {allowed_positions}")

    @property
    def salary(self):
        """Getter for salary"""
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        """Setter for salary with validation"""
        if new_salary > 0:
            self._salary = new_salary
        else:
            raise ValueError("Salary must be a positive number!")

    def __str__(self):
        return f"{self.name} ({self.position}) - Salary: ${self.salary}"
