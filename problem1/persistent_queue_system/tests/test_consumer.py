import os
import pytest
from persistent_queue_system.consumer import Consumer
from persistent_queue_system.queue.sqlite_queue import PersistentQSQLite

@pytest.fixture
def consumer():
    return Consumer(queue_db=":memory:")

def test_consumer_processes_job(consumer):
    queue = PersistentQSQLite(":memory:")
    queue.enqueue("test_job.txt")
    consumer.process_job("test_job.txt")
    assert queue.get_status("test_job.txt") == "done"
