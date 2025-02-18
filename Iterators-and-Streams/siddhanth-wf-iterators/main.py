from siddhanth_wf_iterators.basic_iterator import NumberIterator
from siddhanth_wf_iterators.file_iterator import FileIterator
from siddhanth_wf_iterators.file_generator import file_generator
from siddhanth_wf_iterators.filter_generator import filtered_file_generator
from siddhanth_wf_iterators.stream_processing import process_numbers
from siddhanth_wf_iterators.pipeline import word_count_pipeline
from siddhanth_wf_iterators.chaining import combined_iterators
from siddhanth_wf_iterators.efficient_processing import efficient_file_pipeline
from siddhanth_wf_iterators.error_handling import safe_file_generator
from siddhanth_wf_iterators.advanced_pipeline import process_and_write_output

def run_all_tests():
    print("\n--- Running Basic Iterator ---")
    for num in NumberIterator():
        print(num, end=" ")

    print("\n\n--- Running File Iterator ---")
    for line in FileIterator("data/sample.txt"):
        print(line)

    print("\n--- Running File Generator ---")
    for line in file_generator("data/sample.txt"):
        print(line)

    print("\n--- Running Filtered File Generator ---")
    for line in filtered_file_generator("data/sample.txt", "error"):
        print(line)

    print("\n--- Running Stream Processing ---")
    for num in process_numbers(range(1, 6)):
        print(num, end=" ")

    print("\n\n--- Running File Processing Pipeline ---")
    for count in word_count_pipeline("data/sample.txt", "error"):
        print(count)

    print("\n--- Running Chained Iterators ---")
    for num in combined_iterators(range(1, 5), range(5, 10)):
        print(num, end=" ")

    print("\n\n--- Running Efficient File Handling ---")
    for word_count in efficient_file_pipeline("data/large_file.txt", "error"):
        print(word_count)

    print("\n--- Running Exception Handling ---")
    for line in safe_file_generator("data/missing.txt", "error"):
        print(line)

    print("\n--- Running Advanced Processing ---")
    process_and_write_output(["data/sample.txt"], "error", "data/output.txt")
    print("Processed output written to data/output.txt")

if __name__ == "__main__":
    run_all_tests()
