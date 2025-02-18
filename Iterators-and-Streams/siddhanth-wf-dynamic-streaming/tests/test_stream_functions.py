from siddhanth_wf_dynamic_streaming.stream_functions import number_the_lines

def test_number_the_lines():
    lines = iter(["Hello", "World"])
    result = list(number_the_lines(lines))
    assert result == ["1: Hello", "2: World"]
