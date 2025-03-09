import time
import datetime
import logging
from persistent_queue_system.queue.sqlite_queue import PersistentQSQLite

class Manager:
    """
    Advanced job management with comprehensive monitoring and recovery.
    """
    def __init__(
        self, 
        queue_db="queue.db", 
        stale_threshold_seconds=3600,  # 1 hour default
        max_job_age_days=7
    ):
        """
        Initialize job manager with configurable thresholds.
        
        Args:
            queue_db (str): Database path
            stale_threshold_seconds (int): Time after which a job is considered stale
            max_job_age_days (int): Maximum allowable job lifetime
        """
        self.queue = PersistentQSQLite()
        self.stale_threshold = stale_threshold_seconds
        self.max_job_age_days = max_job_age_days
        
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def check_job_health(self):
        """
        Comprehensive system-wide job health check and recovery.
        Handles stale jobs, prevents job starvation.
        """
        job_health = self.queue.monitor_job_health()
        self.logger.info(f"Job Health Status: {job_health}")

        # Resubmit or cancel excessively old jobs
        stale_jobs = self.queue.get_jobs_by_status([
            'processing', 'pending', 
            'permanently_failed'
        ])

        now = datetime.datetime.now()
        for job in stale_jobs:
            job_created = datetime.datetime.strptime(
                job['created_at'], "%Y-%m-%d %H:%M:%S"
            )
            job_age = (now - job_created).days

            if job_age > self.max_job_age_days:
                self.logger.warning(
                    f"Job {job['job_id']} exceeded max age. Taking action."
                )
                
                if job['status'] == 'processing':
                    # Force resubmit stale processing jobs
                    self.queue.mark_failed(
                        job['job_id'], 
                        f"Job stalled after {job_age} days"
                    )
                elif job['status'] == 'permanently_failed':
                    # Optionally log or archive extremely old failed jobs
                    self.logger.error(
                        f"Archiving permanently failed job: {job['job_id']}"
                    )

    def run(self):
        """
        Continuous job system monitoring and recovery.
        """
        while True:
            try:
                self.check_job_health()
                time.sleep(300)  # Check every 5 minutes
            except Exception as e:
                self.logger.error(f"Job health check failed: {e}")
                time.sleep(60)  # Wait before retry

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    manager = Manager()
    manager.run()