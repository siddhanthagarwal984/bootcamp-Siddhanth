import os
import time
import random
from persistent_queue_system.queue.sqlite_queue import PersistentQSQLite

class Producer:
    """Producer generates jobs and submits them to the queue."""

    def __init__(self, queue_db="queue.db"):
        self.queue = PersistentQSQLite(queue_db)
        self.output_dir = "jobs"
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_file(self):
        """Generates a random file with sample content."""
        job_id = f"{self.output_dir}/job_{int(time.time())}.txt"
        with open(job_id, "w") as f:
            f.write(f"Job ID: {job_id}\n")
            f.write(f"Random Value: {random.randint(1, 100)}\n")
        return job_id

    def submit_job(self):
        """Creates a job file and submits it to the queue."""
        job_id = self.generate_file()
        print(f"Submitting job: {job_id}")
        self.queue.enqueue(job_id)

    def run(self, interval=5):
        """Continuously submits jobs at regular intervals."""
        while True:
            self.submit_job()
            time.sleep(interval)

if __name__ == "__main__":
    producer = Producer()
    producer.run()
