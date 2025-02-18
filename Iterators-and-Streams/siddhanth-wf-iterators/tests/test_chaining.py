import pytest
from siddhanth_wf_iterators.chaining import combined_iterators

def test_combined_iterators():
    assert list(combined_iterators(range(1, 3), range(3, 5))) == [1, 2, 3, 4]

if __name__ == "__main__":
    pytest.main()
