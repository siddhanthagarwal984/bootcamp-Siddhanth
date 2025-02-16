from company import Company
from employee import Employee
from project import Project
from department import Department

# Company setup
company = Company("TechCorp")
it_dept = Department("IT")
company.add_department(it_dept)

# Employees
alice = Employee("Alice", 101, "Engineer")
it_dept.add_employee(alice)

# Project assignment
project_a = Project("AI Development", it_dept)
company.add_project(project_a)
company.assign_employee_to_project(alice, project_a)

print(f"Projects: {company.list_projects()}")
