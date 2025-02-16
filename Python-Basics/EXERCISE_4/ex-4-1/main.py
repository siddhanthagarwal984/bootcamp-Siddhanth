from decorators import simple_logger

@simple_logger
def greet():
    print("Hello, World!")

greet()
