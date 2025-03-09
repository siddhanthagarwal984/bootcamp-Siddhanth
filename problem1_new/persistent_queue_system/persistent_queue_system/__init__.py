"""
Persistent Queue System

A robust, scalable job queue management system with SQLite backend.

Key Components:
- Queue Management
- Job Processing
- Monitoring and Recovery
"""

__version__ = "0.1.0"
__all__ = [
    'queue',  # Subpackage for queue implementations
    'producer',
    'consumer',
    'manager',
    'admin',
    'ops'
]


