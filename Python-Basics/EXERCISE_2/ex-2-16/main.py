from employee import Employee
from department import Department

# Employees can exist without a department
alice = Employee("Alice", 101, "Engineer")
bob = Employee("Bob", 102, "Designer")

# Creating a department and adding employees
it_dept = Department("IT")
it_dept.add_employee(alice)
it_dept.add_employee(bob)

print(f"Department: {it_dept.name}, Employees: {it_dept.list_employees()}")
