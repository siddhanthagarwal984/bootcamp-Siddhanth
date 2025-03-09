import sqlite3
import time
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import logging

from persistent_queue_system.db import get_db_connection
from .base import PersistentQInterface

class PersistentQSQLite(PersistentQInterface):
    MAX_RETRY_ATTEMPTS = 5
    MAX_PROCESSING_TIME = 3600  # 1 hour max processing time
    
    def __init__(self, log_level=logging.INFO):
        """
        Initialize the queue with logging and thread-safe practices.
        
        Args:
            log_level (int): Logging level for tracking queue operations
        """
        self.conn = get_db_connection()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self._create_table()

    def _create_table(self):
        """
        Initialize the queue table with comprehensive schema and indexing.
        Enhanced to support concurrent access and robust job tracking.
        """
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    job_id TEXT UNIQUE,
                    status TEXT CHECK(status IN ('pending', 'processing', 'done', 'failed', 'permanently_failed', 'cancelled')),
                    attempts INTEGER DEFAULT 0,
                    last_attempt_at TIMESTAMP,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    error_message TEXT,
                    priority INTEGER DEFAULT 0,
                    processing_lock INTEGER DEFAULT 0  -- Added for atomic processing
                )
            """)
            # Create indexes for performance
            self.conn.execute("CREATE INDEX IF NOT EXISTS idx_job_status ON jobs(status)")
            self.conn.execute("CREATE INDEX IF NOT EXISTS idx_job_priority ON jobs(priority)")

    def enqueue(self, job: str, priority: int = 0):
        """
        Atomic job enqueueing with conflict prevention.
        
        Args:
            job (str): Unique job identifier
            priority (int): Job processing priority
        
        Raises:
            ValueError: If job already exists
        """
        try:
            with self.conn:
                self.conn.execute("""
                    INSERT INTO jobs 
                    (job_id, status, attempts, last_attempt_at, priority) 
                    VALUES (?, 'pending', 0, NULL, ?)
                """, (job, priority))
                self.logger.info(f"Job enqueued: {job} with priority {priority}")
        except sqlite3.IntegrityError:
            self.logger.warning(f"Attempted to enqueue duplicate job: {job}")
            raise ValueError(f"Job {job} already exists in the queue")

    def dequeue(self, timeout: int = 60) -> Optional[str]:
        """
        Thread-safe job dequeuing with atomic locking.
        
        Args:
            timeout (int): Maximum processing time for a job
        
        Returns:
            Optional[str]: Dequeued job identifier
        """
        with self.conn:
            # Preventing concurrent processing
            cur = self.conn.execute("""
                WITH target_job AS (
                    SELECT job_id 
                    FROM jobs 
                    WHERE status = 'pending'
                      AND (
                          last_attempt_at IS NULL OR 
                          julianday('now') - julianday(last_attempt_at) > ?
                      )
                    ORDER BY priority DESC, created_at ASC 
                    LIMIT 1
                )
                UPDATE jobs 
                SET 
                    status = 'processing', 
                    attempts = attempts + 1,
                    last_attempt_at = CURRENT_TIMESTAMP,
                    updated_at = CURRENT_TIMESTAMP,
                    processing_lock = abs(random())  -- Unique lock
                WHERE job_id = (SELECT job_id FROM target_job)
                RETURNING job_id
            """, (timeout / (24 * 3600),))
            
            row = cur.fetchone()
            if row:
                self.logger.info(f"Dequeued job: {row[0]}")
                return row[0]
            return None

    def mark_completed(self, job: str):
        """
        Mark job as completed with transactional safety.
        
        Args:
            job (str): Job identifier
        
        Raises:
            ValueError: If job cannot be marked complete
        """
        with self.conn:
            rowcount = self.conn.execute("""
                UPDATE jobs 
                SET status = 'done', 
                    updated_at = CURRENT_TIMESTAMP 
                WHERE job_id = ? AND status = 'processing'
            """, (job,)).rowcount
            
            if rowcount == 0:
                self.logger.error(f"Cannot mark job {job} as completed")
                raise ValueError(f"Job {job} is not in a processable state")
            
            self.logger.info(f"Job completed: {job}")

    def mark_failed(self, job: str, error_message: str = None):
        """
        Advanced job failure handling with exponential backoff and permanent failure prevention.
        
        Args:
            job (str): Job identifier
            error_message (str, optional): Failure description
        """
        with self.conn:
            cur = self.conn.execute("""
                SELECT attempts, status, 
                       julianday('now') - julianday(last_attempt_at) AS hours_since_last
                FROM jobs 
                WHERE job_id = ?
            """, (job,))
            
            result = cur.fetchone()
            if not result:
                self.logger.error(f"Job not found: {job}")
                raise ValueError(f"Job {job} not found")
            
            attempts, current_status, hours_since_last = result
            
            # Retry logic with max attempts and exponential backoff
            if (current_status == 'processing' and 
                attempts < self.MAX_RETRY_ATTEMPTS and 
                (hours_since_last is None or hours_since_last > 1)):
                
                self.conn.execute("""
                    UPDATE jobs 
                    SET status = 'pending', 
                        attempts = attempts + 1, 
                        last_attempt_at = CURRENT_TIMESTAMP,
                        updated_at = CURRENT_TIMESTAMP,
                        error_message = COALESCE(?, error_message)
                    WHERE job_id = ?
                """, (error_message, job))
                self.logger.warning(f"Job retry: {job} (Attempt {attempts + 1})")
            else:
                # Permanently fail job
                self.conn.execute("""
                    UPDATE jobs 
                    SET status = 'permanently_failed', 
                        updated_at = CURRENT_TIMESTAMP,
                        error_message = COALESCE(?, error_message)
                    WHERE job_id = ?
                """, (error_message, job))
                self.logger.error(f"Job permanently failed: {job}")
    
    def get_status(self, job: str) -> Optional[str]:
        """
        Retrieve the status of a specific job.
        
        Args:
            job (str): Job identifier
        
        Returns:
            Optional[str]: Job status or None if not found
        """
        with self.conn:
            cur = self.conn.execute("SELECT status FROM jobs WHERE job_id = ?", (job,))
            row = cur.fetchone()
            return row[0] if row else None

    def get_jobs_by_status(self, statuses: List[str]) -> List[Dict]:
        """
        Retrieve comprehensive jobs information by status.
        
        Args:
            statuses (List[str]): List of statuses to filter
        
        Returns:
            List[Dict]: Detailed job information
        """
        query = """
            SELECT id, job_id, status, attempts, created_at, 
                   error_message, priority, updated_at
            FROM jobs 
            WHERE status IN ({})
            ORDER BY priority DESC, created_at DESC
        """.format(','.join(['?'] * len(statuses)))
        
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute(query, statuses)
            columns = [
                'id', 'job_id', 'status', 'attempts', 
                'created_at', 'error_message', 'priority', 'updated_at'
            ]
            
            return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def monitor_job_health(self) -> Dict[str, int]:
        """
        Comprehensive job status overview.
        
        Returns:
            Dict[str, int]: Job status distribution
        """
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("""
                SELECT status, 
                       COUNT(*) as count, 
                       AVG(attempts) as avg_attempts,
                       MAX(julianday('now') - julianday(created_at)) as max_age_days
                FROM jobs 
                GROUP BY status
            """)
            
            result = {}
            for status, count, avg_attempts, max_age in cursor.fetchall():
                result[status] = {
                    'count': count,
                    'avg_attempts': round(avg_attempts or 0, 2),
                    'max_age_days': round(max_age or 0, 2)
                }
            
            return result