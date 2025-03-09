import os
import time
import random
import logging
from persistent_queue_system.queue.sqlite_queue import PersistentQSQLite

class Producer:
    """Generates and submits jobs to the queue."""

    def __init__(self, queue_db="queue.db", output_dir="jobs"):
        """
        Initialize producer with configurable queue and output directory.
        
        Args:
            queue_db (str): Queue database path
            output_dir (str): Directory to store job files
        """
        self.queue = PersistentQSQLite()
        self.output_dir = output_dir
        self.logger = logging.getLogger(__name__)
        
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_file(self):
        """
        Generate a unique job file with random content.
        
        Returns:
            str: Path to generated job file
        """
        job_id = f"{self.output_dir}/job_{int(time.time())}_{random.randint(1000, 9999)}.txt"
        try:
            with open(job_id, "w") as f:
                f.write(f"Job ID: {job_id}\n")
                f.write(f"Timestamp: {time.ctime()}\n")
                f.write(f"Random Value: {random.randint(1, 1000)}\n")
            
            self.logger.info(f"Job file created: {job_id}")
            return job_id
        except IOError as e:
            self.logger.error(f"File generation error: {e}")
            raise

    def submit_job(self, priority: int = 0):
        """
        Create a job file and submit to queue.
        
        Args:
            priority (int): Job processing priority
        """
        try:
            job_id = self.generate_file()
            self.queue.enqueue(job_id, priority)
            self.logger.info(f"Job submitted: {job_id}")
        except Exception as e:
            self.logger.error(f"Job submission failed: {e}")

    def run(self, interval: int = 5):
        """
        Continuously submit jobs at specified interval.
        
        Args:
            interval (int): Seconds between job submissions
        """
        while True:
            try:
                self.submit_job()
                time.sleep(interval)
            except KeyboardInterrupt:
                self.logger.info("Producer stopped.")
                break
            except Exception as e:
                self.logger.error(f"Unexpected error: {e}")
                time.sleep(interval)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    producer = Producer()
    producer.run()