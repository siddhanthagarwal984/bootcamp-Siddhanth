from company import Company
from department import Department
from project import Project
from employee import Employee

# Creating a company
company = Company("TechCorp")

# Creating departments
it_dept = Department("IT")
company.add_department(it_dept)

# Creating employees
alice = Employee("Alice", 101, "Engineer")
it_dept.add_employee(alice)

# Creating a project
project_a = Project("AI Development", it_dept)
company.add_project(project_a)

print(f"Company: {company.name}, Departments: {company.list_departments()}")
