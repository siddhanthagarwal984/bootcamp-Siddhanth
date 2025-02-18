import pytest
from siddhanth_wf_iterators.stream_processing import process_numbers

def test_process_numbers():
    assert list(process_numbers(range(1, 6))) == [2, 4, 6, 8, 10]

if __name__ == "__main__":
    pytest.main()
