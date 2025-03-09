import sqlite3
import logging
import atexit

DB_PATH = "queue.db"

class SQLiteConnection:
    """
    Thread-safe singleton SQLite connection manager.
    """
    _instance = None
    _logger = logging.getLogger(__name__)

    @classmethod
    def get_connection(cls):
        """
        Returns a shared, thread-safe database connection.
        
        Returns:
            sqlite3.Connection: Shared database connection
        """
        if cls._instance is None:
            try:
                cls._instance = sqlite3.connect(
                    DB_PATH, 
                    check_same_thread=False, 
                    isolation_level=None  # Enable auto-commit
                )
                cls._logger.info(f"Database connection established: {DB_PATH}")
            except sqlite3.Error as e:
                cls._logger.error(f"Database connection error: {e}")
                raise
        return cls._instance

def get_db_connection():
    """Convenience function to get database connection."""
    return SQLiteConnection.get_connection()

def close_connection():
    """Close the database connection on exit."""
    if SQLiteConnection._instance:
        SQLiteConnection._instance.close()
        logging.getLogger(__name__).info("Database connection closed.")

# Register connection closure on exit
atexit.register(close_connection)