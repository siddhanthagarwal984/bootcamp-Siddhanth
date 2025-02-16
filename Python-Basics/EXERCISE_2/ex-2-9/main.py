from employee import Employee
from department import Department

# Creating employees
emp1 = Employee("Alice Johnson", 101, "Software Engineer")
emp2 = Employee("Bob Smith", 102, "Project Manager")

# Creating a department and adding employees
dept = Department("IT Department")
dept.add_employee(emp1)
dept.add_employee(emp2)

# Displaying department details
print(f"Department: {dept.name}")
print("Employees:", dept.list_employees())
