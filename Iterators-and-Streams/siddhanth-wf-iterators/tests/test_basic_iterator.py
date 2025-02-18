import pytest
from siddhanth_wf_iterators.basic_iterator import NumberIterator

def test_basic_iterator():
    assert list(NumberIterator()) == list(range(1, 11))

if __name__ == "__main__":
    pytest.main()
