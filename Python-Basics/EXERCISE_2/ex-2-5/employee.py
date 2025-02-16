class Employee:
    def __init__(self, name, emp_id, position):
        self.name = name
        self.emp_id = emp_id
        self.position = position

    def update_position(self, new_position):
        """Updates the employee's position"""
        self.position = new_position

    def display_info(self):
        """Displays employee information"""
        return f"Employee Name: {self.name}, ID: {self.emp_id}, Position: {self.position}"
