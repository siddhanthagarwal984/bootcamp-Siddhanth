import time
from persistent_queue_system.queue.sqlite_queue import PersistentQSQLite

class Manager:
    """Manager handles job management tasks."""

    def __init__(self, queue_db="queue.db"):
        self.queue = PersistentQSQLite(queue_db)

    def resubmit_job(self, job_id):
        """Resubmits a job to the queue."""
        print(f"Resubmitting job: {job_id}")
        self.queue.enqueue(job_id)

    def mark_unprocessable(self, job_id):
        """Marks a job as unprocessable."""
        print(f"Marking job as unprocessable: {job_id}")
        # Logic to mark the job in the database or queue

    def run(self):
        """Run the manager console."""
        while True:
            # Placeholder for manager console logic
            time.sleep(5)

if __name__ == "__main__":
    manager = Manager()
    manager.run()
