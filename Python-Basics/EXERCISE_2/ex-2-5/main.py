from employee import Employee

# Creating an Employee instance
emp = Employee("Charlie Davis", 103, "Developer")

# Display initial info
print(emp.display_info())

# Update position
emp.update_position("Senior Developer")

# Display updated info
print(emp.display_info())
