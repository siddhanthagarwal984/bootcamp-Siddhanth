from typing import Callable, Iterator
from siddhanth_wf_dynamic_streaming.processing_functions import upper_case, lower_case, remove_stop_words, uk_to_us

StringFunction = Callable[[str], str]
StreamFunction = Callable[[Iterator[str]], Iterator[str]]

def string_to_stream_function(in_function: StringFunction) -> StreamFunction:
    """Converts a string function into a streaming function."""
    def wrapped(iterator: Iterator[str]) -> Iterator[str]:
        for line in iterator:
            yield in_function(line)
    return wrapped

# Adapt existing functions to stream functions
stream_upper_case = string_to_stream_function(upper_case)
stream_lower_case = string_to_stream_function(lower_case)
stream_remove_stop_words = string_to_stream_function(remove_stop_words)
stream_uk_to_us = string_to_stream_function(uk_to_us)
