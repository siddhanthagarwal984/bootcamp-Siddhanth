import pytest
from siddhanth_wf_iterators.filter_generator import filtered_file_generator

def test_filtered_file_generator(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Error: issue\nNo error\nCritical Error")
    assert list(filtered_file_generator(str(test_file), "Error")) == ["Error: issue", "Critical Error"]

if __name__ == "__main__":
    pytest.main()
