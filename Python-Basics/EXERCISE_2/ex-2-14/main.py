from employee import Employee
from department import Department

emp = Employee("Alice", 101, "Engineer", 60000)
dept = Department("IT")
dept.add_employee(emp)

print(emp)   # Calls __str__
print(repr(emp))  # Calls __repr__
print(dept)  # Calls __str__
