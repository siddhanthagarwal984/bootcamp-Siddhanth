from dynamic_class import create_dynamic_class

DynamicClass = create_dynamic_class()
instance = DynamicClass()

print(f"Attribute: {instance.attribute}")
print(f"Method Output: {instance.method()}")
