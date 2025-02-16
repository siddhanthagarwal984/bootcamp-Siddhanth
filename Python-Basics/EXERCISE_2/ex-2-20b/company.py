from department import Department
from project import Project

class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.projects = []

    def add_department(self, department):
        self.departments.append(department)

    def add_project(self, project):
        self.projects.append(project)

    def assign_employee_to_project(self, employee, project):
        project.assign_employee(employee)

    def list_projects(self):
        return ", ".join(proj.name for proj in self.projects)
