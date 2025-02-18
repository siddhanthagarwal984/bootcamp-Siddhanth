import pytest
from siddhanth_wf_iterators.advanced_pipeline import process_and_write_output

def test_process_and_write_output(tmp_path):
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "output.txt"
    input_file.write_text("Error found here\nNo issue\nCritical Error occurred")
    process_and_write_output([str(input_file)], "Error", str(output_file))
    assert output_file.read_text().strip() == "3\n3"

if __name__ == "__main__":
    pytest.main()
