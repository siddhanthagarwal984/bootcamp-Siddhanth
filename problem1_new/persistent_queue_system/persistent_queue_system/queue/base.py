from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Any

class PersistentQInterface(ABC):
    """
    Abstract base class defining a comprehensive interface for persistent queues.
    
    Supports:
    - Job enqueueing with priority
    - Robust job dequeuing
    - Job status management
    - System-wide job monitoring
    """

    @abstractmethod
    def enqueue(self, job: str, priority: int = 0):
        """
        Add a job to the queue.
        
        Args:
            job (str): Unique job identifier
            priority (int, optional): Job processing priority
        
        Raises:
            ValueError: If job already exists
        """
        pass

    @abstractmethod
    def dequeue(self, timeout: int = 60) -> Optional[str]:
        """
        Retrieve and lock a job for processing.
        
        Args:
            timeout (int): Maximum processing time for a job
        
        Returns:
            Optional[str]: Job identifier if available
        """
        pass

    @abstractmethod
    def mark_completed(self, job: str):
        """
        Mark a job as successfully completed.
        
        Args:
            job (str): Job identifier
        
        Raises:
            ValueError: If job cannot be marked complete
        """
        pass

    @abstractmethod
    def mark_failed(self, job: str, error_message: str = None):
        """
        Handle job failure with retry mechanisms.
        
        Args:
            job (str): Job identifier
            error_message (str, optional): Failure description
        """
        pass

    @abstractmethod
    def get_status(self, job: str) -> Optional[str]:
        """
        Retrieve the current status of a specific job.
        
        Args:
            job (str): Job identifier
        
        Returns:
            Optional[str]: Job status
        """
        pass

    @abstractmethod
    def get_jobs_by_status(self, statuses: List[str]) -> List[Dict]:
        """
        Retrieve jobs filtered by status.
        
        Args:
            statuses (List[str]): Job statuses to retrieve
        
        Returns:
            List[Dict]: Matching job details
        """
        pass

    @abstractmethod
    def monitor_job_health(self) -> Dict[str, Any]:
        """
        Provide an overview of job statuses in the system.
        
        Returns:
            Dict[str, Any]: Job status distribution and health metrics
        """
        pass