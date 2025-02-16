class Employee:
    def __init__(self, name, emp_id, position, salary):
        self.name = name
        self.emp_id = emp_id
        self._position = position  # Private attribute
        self._salary = salary  # Private attribute

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        if new_position in ["Engineer", "Manager", "Designer"]:
            self._position = new_position
        else:
            raise ValueError("Invalid position!")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary
        else:
            raise ValueError("Salary must be positive!")
