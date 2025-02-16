class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def __str__(self):
        return f"Company: {self.name}, Departments: {[dept.name for dept in self.departments]}"

# Example usage
company = Company("TechCorp")
print(company)
