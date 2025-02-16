from employee import Employee
from department import Department

# Creating a department
dept = Department("IT")

# Creating employees
emp1 = Employee("Alice", 101, "Engineer", 60000)
emp2 = Employee("Bob", 102, "Manager", 80000)

# Adding employees to the department
dept.add_employee(emp1)
dept.add_employee(emp2)

# Retrieving an employee
retrieved_emp = dept.get_employee(101)
print(f"Retrieved: {retrieved_emp.name} - {retrieved_emp.position}")
