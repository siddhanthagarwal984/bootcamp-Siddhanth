from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals with an abstract property 'sound'."""
    
    @property
    @abstractmethod
    def sound(self):
        """Abstract property that must be implemented in subclasses."""
        pass
