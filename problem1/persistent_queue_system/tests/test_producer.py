import os
import pytest
from persistent_queue_system.producer import Producer

@pytest.fixture
def producer():
    return Producer(queue_db=":memory:")

def test_producer_creates_file(producer):
    job_id = producer.generate_file()
    assert os.path.exists(job_id)
