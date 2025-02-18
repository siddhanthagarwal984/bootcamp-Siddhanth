import pytest
from siddhanth_wf_iterators.error_handling import safe_file_generator

def test_safe_file_generator():
    assert list(safe_file_generator("non_existent.txt", "Error")) == []

if __name__ == "__main__":
    pytest.main()
