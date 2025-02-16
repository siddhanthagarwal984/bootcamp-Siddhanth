from employee import Employee
from manager import Manager

# Creating employees
emp1 = Employee("Alice Johnson", 101, "Software Engineer")
emp2 = Employee("Bob Smith", 102, "Project Manager")

# Creating a manager and assigning subordinates
mgr = Manager("Charlie Davis", 103, "Team Lead")
mgr.add_subordinate(emp1)
mgr.add_subordinate(emp2)

# Displaying subordinates
print(f"Manager: {mgr.name}")
print("Subordinates:", mgr.list_subordinates())
