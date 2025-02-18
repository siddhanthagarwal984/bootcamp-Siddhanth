import pytest
from siddhanth_wf_iterators.pipeline import word_count_pipeline

def test_word_count_pipeline(tmp_path):
    test_file = tmp_path / "test_file.txt"
    test_file.write_text("Error found here\nNothing wrong\nCritical Error occurred")
    assert list(word_count_pipeline(str(test_file), "Error")) == [3, 3]

if __name__ == "__main__":
    pytest.main()
