import sqlite3
import atexit
DB_PATH = "queue.db"

class SQLiteConnection:
    _instance = None

    @classmethod
    def get_connection(cls):
        if cls._instance is None:
            cls._instance = sqlite3.connect(DB_PATH, check_same_thread=False)
        return cls._instance

def get_db_connection():
    """Returns a shared database connection."""
    return SQLiteConnection.get_connection()




def close_connection():
    """Closes the database connection on exit."""
    if SQLiteConnection._instance:
        SQLiteConnection._instance.close()

atexit.register(close_connection)
