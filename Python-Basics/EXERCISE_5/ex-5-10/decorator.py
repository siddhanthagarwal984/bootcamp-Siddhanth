def add_method(cls):
    """Class decorator that adds a new method to the class."""
    def new_method(self):
        return "New method added by decorator!"
    
    cls.new_method = new_method
    return cls
