from mixin import JsonMixin

class User(JsonMixin):
    """User class utilizing the JsonMixin."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
