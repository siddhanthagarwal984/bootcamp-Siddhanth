from animal import Animal

class Dog(Animal):
    """Dog class implementing the abstract property sound."""
    
    @property
    def sound(self):
        return "Bark"
