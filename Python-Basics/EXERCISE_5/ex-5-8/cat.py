from animal import Animal

class Cat(Animal):
    """Cat class implementing the abstract property sound."""
    
    @property
    def sound(self):
        return "Meow"
