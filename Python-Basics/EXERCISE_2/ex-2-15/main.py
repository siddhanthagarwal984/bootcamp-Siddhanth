from employee import Employee
from manager import Manager
from department import Department

# Creating objects
emp = Employee("Alice", 101, "Engineer", 60000)
mgr = Manager("Bob", 102, "Manager", 80000, [emp])
dept = Department("IT")
dept.add_employee(emp)
dept.add_employee(mgr)

# Displaying special methods
print(emp)  # Calls __str__
print(repr(emp))  # Calls __repr__
print(mgr)  # Calls __str__
print(repr(mgr))  # Calls __repr__
print(dept)  # Calls __str__
print(repr(dept))  # Calls __repr__
