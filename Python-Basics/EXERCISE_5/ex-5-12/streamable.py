from abc import ABC, abstractmethod

class Streamable(ABC):
    """Abstract interface for streaming content."""

    @abstractmethod
    def stream(self):
        """Abstract method that must be implemented in subclasses."""
        pass
