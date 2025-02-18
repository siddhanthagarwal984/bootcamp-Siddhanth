from itertools import chain

from siddhanth_wf_iterators.error_handling import safe_file_generator
from siddhanth_wf_iterators.pipeline import count_words

def multi_file_generator(filenames, keyword):
    for filename in filenames:
        yield from safe_file_generator(filename, keyword)

def process_and_write_output(input_files, filter_word, output_file):
    with open(output_file, "w") as out:
        for file in input_files:
            with open(file, "r") as f:
                for line in f:
                    if filter_word in line:
                        word_count = len(line.split())
                        out.write(f"{word_count}\n")  # Only write the number

