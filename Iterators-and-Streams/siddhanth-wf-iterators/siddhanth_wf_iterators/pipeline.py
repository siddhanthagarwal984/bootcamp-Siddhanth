from siddhanth_wf_iterators.filter_generator import filtered_file_generator


def count_words(line):
    return len(line.split())

def word_count_pipeline(filename, keyword):
    return (count_words(line) for line in filtered_file_generator(filename, keyword))
