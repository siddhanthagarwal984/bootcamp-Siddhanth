import time
import random
import logging
from persistent_queue_system.queue.sqlite_queue import PersistentQSQLite

class Consumer:
    """Fetches and processes jobs from the queue."""

    def __init__(self, queue_db="queue.db"):
        """
        Initialize consumer with queue connection.
        
        Args:
            queue_db (str): Queue database path
        """
        self.queue = PersistentQSQLite()
        self.logger = logging.getLogger(__name__)

    def process_job(self, job_id: str):
        """
        Process a job by appending processing metadata.
        
        Args:
            job_id (str): Job file path
        """
        try:
            with open(job_id, "a") as f:
                f.write(f"Processed at: {time.ctime()}\n")
                f.write(f"Processing Duration: {random.uniform(0.1, 2.0)} seconds\n")
            
            self.queue.mark_completed(job_id)
            self.logger.info(f"Job completed: {job_id}")
        
        except Exception as e:
            self.logger.error(f"Job processing error: {job_id}")
            self.queue.mark_failed(job_id, str(e))

    def run(self):
        """Continuously fetch and process jobs."""
        while True:
            try:
                job_id = self.queue.dequeue()
                
                if job_id:
                    # Simulate variable processing time
                    time.sleep(random.uniform(7.0, 15.0))
                    #self.logger.info(f"Processing job: {job_id}. Sleeping for {delay:.2f} seconds.")
                    self.process_job(job_id)
                else:
                    self.logger.info("No jobs available. Waiting...")
                    time.sleep(5)
            
            except KeyboardInterrupt:
                self.logger.info("Consumer stopped.")
                break
            except Exception as e:
                self.logger.error(f"Unexpected error: {e}")
                time.sleep(5)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    consumer = Consumer()
    consumer.run()