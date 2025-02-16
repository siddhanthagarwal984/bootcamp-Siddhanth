from employee import Employee

# Creating an Employee instance
emp = Employee("Alice", 101, "Engineer", 60000)

# Accessing attributes using properties
print(emp.position)  # Engineer
print(emp.salary)  # 60000

# Updating position correctly
emp.position = "Manager"
print(emp.position)  # Manager

# Attempting an invalid position
try:
    emp.position = "Intern"
except ValueError as e:
    print(e)  # "Invalid position! Allowed: ['Engineer', 'Manager', 'Designer', 'HR']"

# Updating salary correctly
emp.salary = 75000
print(emp.salary)  # 75000

# Attempting to set a negative salary
try:
    emp.salary = -5000
except ValueError as e:
    print(e)  # "Salary must be a positive number!"
