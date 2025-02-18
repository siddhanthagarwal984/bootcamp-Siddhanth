from siddhanth_wf_iterators.filter_generator import filtered_file_generator
from siddhanth_wf_iterators.pipeline import count_words


def efficient_file_pipeline(file_path, filter_word):
    with open(file_path, "r") as f:
        return [len(line.split()) for line in f if filter_word in line][:1]  # Only return the first match
