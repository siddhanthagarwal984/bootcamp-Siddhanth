from employee import Employee
from department import Department

# Creating employees
emp1 = Employee("Alice Johnson", 101, "Software Engineer")
emp2 = Employee("Bob Smith", 102, "Project Manager")

# Creating a department with employees
dept = Department("IT Department", [emp1, emp2])

# Displaying department details
print(f"Department: {dept.name}")
print("Employees:", dept.list_employees())

# Adding a new employee
emp3 = Employee("Charlie Davis", 103, "DevOps Engineer")
dept.add_employee(emp3)

# Displaying updated department details
print("Updated Employees:", dept.list_employees())
