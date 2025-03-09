"""
Persistent Queue Implementation Package

Provides an abstract interface and concrete implementations 
for a robust, persistent queue system.
"""

from .base import PersistentQInterface
from .sqlite_queue import PersistentQSQLite

__all__ = [
    'PersistentQInterface',  # Abstract base interface
    'PersistentQSQLite',     # SQLite-based concrete implementation
]