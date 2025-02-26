import time
import datetime
from persistent_queue_system.queue.sqlite_queue import PersistentQSQLite

class Manager:
    """Manager handles job management tasks, including automatic resubmission of stale jobs."""

    def __init__(self, queue_db="queue.db", stale_threshold_seconds=60):
        self.queue = PersistentQSQLite(queue_db)
        self.stale_threshold = stale_threshold_seconds  # Time in seconds after which a job is considered stale

    def resubmit_job(self, job_id):
        """Resubmits a job to the queue by re-enqueuing it."""
        print(f"Resubmitting job: {job_id}")
        self.queue.enqueue(job_id)

    def mark_unprocessable(self, job_id):
        """Marks a job as unprocessable."""
        print(f"Marking job as unprocessable: {job_id}")
        # Logic to mark the job in the database or queue can be added here

    def check_stale_jobs(self):
        """Checks for jobs that have been in 'processing' state too long and resubmits them."""
        all_jobs = self.queue.get_all_jobs()
        now = datetime.datetime.now()
        for job in all_jobs:
            if job['status'] == 'processing':
                try:
                    # Assuming the created_at field is in the format "YYYY-MM-DD HH:MM:SS"
                    job_time = datetime.datetime.strptime(job['created_at'], "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    print(f"Error parsing timestamp for job: {job}")
                    continue
                elapsed = (now - job_time).total_seconds()
                if elapsed > self.stale_threshold:
                    print(f"Job {job['job_id']} has been processing for {elapsed} seconds. Resubmitting.")
                    self.resubmit_job(job['job_id'])

    def run(self):
        """Run the manager console and periodically check for stale jobs."""
        while True:
            self.check_stale_jobs()
            time.sleep(30)  # Checking every 30 seconds

if __name__ == "__main__":
    manager = Manager(stale_threshold_seconds=60)  # Resubmit jobs processing for more than 60 seconds
    manager.run()
