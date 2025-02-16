from decorator import add_method

@add_method
class TestClass:
    def existing_method(self):
        return "Existing method in class."
