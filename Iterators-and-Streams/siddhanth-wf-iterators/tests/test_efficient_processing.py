import pytest
from siddhanth_wf_iterators.efficient_processing import efficient_file_pipeline

def test_efficient_file_pipeline(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Error occurred\nNo issue\nMajor Error detected")
    assert list(efficient_file_pipeline(str(test_file), "Error")) == [2]

if __name__ == "__main__":
    pytest.main()
