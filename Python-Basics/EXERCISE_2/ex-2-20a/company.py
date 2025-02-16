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

    def list_departments(self):
        return ", ".join(dept.name for dept in self.departments)
