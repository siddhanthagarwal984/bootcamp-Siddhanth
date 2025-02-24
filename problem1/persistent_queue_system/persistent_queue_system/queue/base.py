from abc import ABC, abstractmethod

class PersistentQInterface(ABC):
    """Abstract base class for persistent queues."""

    @abstractmethod
    def enqueue(self, job: str):
        """Add a job to the queue."""
        pass

    @abstractmethod
    def dequeue(self):
        """Retrieve a job from the queue."""
        pass

    @abstractmethod
    def mark_completed(self, job: str):
        """Mark a job as completed."""
        pass

    @abstractmethod
    def get_status(self, job: str):
        """Retrieve job status."""
        pass