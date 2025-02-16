from decorators import prefix_printer

@prefix_printer("LOG:")
def greet():
    print("Hello, World!")

greet()
