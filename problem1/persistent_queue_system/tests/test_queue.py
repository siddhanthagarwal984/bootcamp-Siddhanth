import pytest
from persistent_queue_system.queue.sqlite_queue import PersistentQSQLite

@pytest.fixture
def queue():
    return PersistentQSQLite(":memory:")  # Use in-memory DB for testing

def test_enqueue_and_dequeue(queue):
    queue.enqueue("job1")
    job = queue.dequeue()
    assert job == "job1"

def test_mark_completed(queue):
    queue.enqueue("job2")
    queue.mark_completed("job2")
    assert queue.get_status("job2") == "done"
