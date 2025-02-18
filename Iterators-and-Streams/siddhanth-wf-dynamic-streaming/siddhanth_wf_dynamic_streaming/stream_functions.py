from typing import Iterator

def number_the_lines(lines: Iterator[str]) -> Iterator[str]:
    """Adds line numbers to each line."""
    for idx, line in enumerate(lines, 1):
        yield f"{idx}: {line}"

def coalesce_empty_lines(lines: Iterator[str]) -> Iterator[str]:
    """Removes multiple consecutive empty lines, leaving only one."""
    prev_blank = False
    for line in lines:
        if line.strip():
            yield line
            prev_blank = False
        elif not prev_blank:
            yield line
            prev_blank = True

def remove_empty_lines(lines: Iterator[str]) -> Iterator[str]:
    """Removes all empty lines."""
    for line in lines:
        if line.strip():
            yield line

def remove_even_lines(lines: Iterator[str]) -> Iterator[str]:
    """Removes all even-numbered lines."""
    for idx, line in enumerate(lines, 1):
        if idx % 2 != 0:
            yield line

def break_lines(lines: Iterator[str], length: int = 20) -> Iterator[str]:
    """Breaks long lines into multiple lines of a given max length."""
    for line in lines:
        while len(line) > length:
            yield line[:length]
            line = line[length:]
        yield line
