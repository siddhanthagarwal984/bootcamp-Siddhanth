import time
import random
from persistent_queue_system.queue.sqlite_queue import PersistentQSQLite

class Consumer:
    """Consumer fetches jobs from the queue and processes them."""

    def __init__(self, queue_db="queue.db"):
        self.queue = PersistentQSQLite(queue_db)

    def process_job(self, job_id):
        """Processes a job by appending a timestamp."""
        print(f"Processing job: {job_id}")
        try:
            with open(job_id, "a") as f:
                f.write(f"Processed at: {time.ctime()}\n")
            self.queue.mark_completed(job_id)
            print(f"Job completed: {job_id}")
        except Exception as e:
            print(f"Error processing {job_id}: {e}")

    def run(self):
        """Continuously fetches and processes jobs from the queue."""
        while True:
            job_id = self.queue.dequeue()
            if job_id:
                time.sleep(random.randint(7, 15))  # Simulating a processing delay
                self.process_job(job_id)
            else:
                print("No jobs available. Sleeping...")
                time.sleep(5)

if __name__ == "__main__":
    consumer = Consumer()
    consumer.run()
