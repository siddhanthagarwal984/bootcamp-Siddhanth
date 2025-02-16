from employee import Employee
from department import Department
from project import Project

# Creating department
it_dept = Department("IT")

# Creating employees
alice = Employee("Alice", 101, "Engineer")
bob = Employee("Bob", 102, "Designer")

# Creating a project and associating with a department
project_a = Project("Website Redesign", it_dept)
project_a.assign_employee(alice)
project_a.assign_employee(bob)

print(f"Project: {project_a.name}, Employees: {project_a.list_employees()}")
