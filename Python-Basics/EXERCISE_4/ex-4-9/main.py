from decorators import validate_args

class Calculator:
    @validate_args
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(3, 5))  # Valid
# print(calc.add(None, 5))  # Raises ValueError
