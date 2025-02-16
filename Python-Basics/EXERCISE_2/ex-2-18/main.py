from employee import Employee

emp = Employee("Alice", 101, "Engineer", 60000)

# Accessing properties
print(emp.position)

# Modifying position safely
emp.position = "Manager"
print(emp.position)

# Attempting invalid position
try:
    emp.position = "Intern"
except ValueError as e:
    print(e)
