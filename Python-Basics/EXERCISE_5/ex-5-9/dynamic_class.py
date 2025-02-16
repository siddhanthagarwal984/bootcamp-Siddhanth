def create_dynamic_class():
    """Creates a new class dynamically using type()."""
    return type("DynamicClass", (object,), {"attribute": "Dynamic Value", "method": lambda self: "Hello from dynamic class!"})
