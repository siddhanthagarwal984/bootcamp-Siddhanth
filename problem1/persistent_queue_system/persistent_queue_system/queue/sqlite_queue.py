import sqlite3
import time
from .base import PersistentQInterface

class PersistentQSQLite(PersistentQInterface):
    def __init__(self, db_path="queue.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._create_table()

    def _create_table(self):
        """Initialize the queue table."""
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    job_id TEXT UNIQUE,
                    status TEXT CHECK( status IN ('pending', 'processing', 'done', 'failed')),
                    attempts INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

    def enqueue(self, job: str):
        """Add a job to the queue with default attempt count."""
        with self.conn:
            self.conn.execute("INSERT INTO jobs (job_id, status, attempts) VALUES (?, 'pending', 0)", (job,))

    def dequeue(self):
        """Retrieve a job from the queue and lock it for processing. Retries if the database is locked."""
        while True:
            try:
                with self.conn:
                    cur = self.conn.execute("""
                        SELECT job_id FROM jobs WHERE status='pending' ORDER BY created_at ASC LIMIT 1
                    """)
                    row = cur.fetchone()
                    if row:
                        job_id = row[0]
                        self.conn.execute("UPDATE jobs SET status='processing' WHERE job_id=?", (job_id,))
                        return job_id
                    return None
            except sqlite3.OperationalError:
                print("Database locked. Retrying in 2 seconds...")
                time.sleep(2)

    def mark_completed(self, job: str):
        """Mark a job as completed."""
        with self.conn:
            self.conn.execute("UPDATE jobs SET status='done' WHERE job_id=?", (job,))

    def mark_failed(self, job: str):
        """If a job fails 3 times, mark it as 'failed', otherwise retry."""
        with self.conn:
            cur = self.conn.execute("SELECT attempts FROM jobs WHERE job_id=?", (job,))
            attempts = cur.fetchone()[0] if cur.fetchone() else 0
            if attempts >= 3:
                self.conn.execute("UPDATE jobs SET status='failed' WHERE job_id=?", (job,))
            else:
                self.conn.execute("UPDATE jobs SET status='pending', attempts=attempts+1 WHERE job_id=?", (job,))

    def get_status(self, job: str):
        """Retrieve the status of a job."""
        with self.conn:
            cur = self.conn.execute("SELECT status FROM jobs WHERE job_id=?", (job,))
            row = cur.fetchone()
            return row[0] if row else None

    def get_all_jobs(self):
        """Retrieve all jobs."""
        query = "SELECT id, job_id, status, attempts, created_at FROM jobs ORDER BY created_at DESC"
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return [{"id": row[0], "job_id": row[1], "status": row[2], "attempts": row[3], "created_at": row[4]} for row in rows]
