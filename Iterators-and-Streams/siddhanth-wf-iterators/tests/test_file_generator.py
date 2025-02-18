import pytest
from siddhanth_wf_iterators.file_generator import file_generator

def test_file_generator(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Line1\nLine2\nLine3")
    assert list(file_generator(str(test_file))) == ["Line1", "Line2", "Line3"]

if __name__ == "__main__":
    pytest.main()
