from test_class import TestClass

obj = TestClass()
print(obj.existing_method())  # Original method
print(obj.new_method())       # Method added by decorator
