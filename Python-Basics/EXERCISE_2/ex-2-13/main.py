from employee import Employee
from department import Department

dept = Department("IT")

# Adding employees
dept.add_employee(Employee("Alice", 101, "Engineer", 60000))
dept.add_employee(Employee("Bob", 102, "Manager", 80000))

# Calculating total salary
print("Total Salary:", dept.total_salary())

# Removing an employee
dept.remove_employee(101)
print("Total Salary after removal:", dept.total_salary())
