import pytest
from siddhanth_wf_iterators.file_iterator import FileIterator

def test_file_iterator(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Line1\nLine2\nLine3")
    assert list(FileIterator(str(test_file))) == ["Line1", "Line2", "Line3"]

if __name__ == "__main__":
    pytest.main()
