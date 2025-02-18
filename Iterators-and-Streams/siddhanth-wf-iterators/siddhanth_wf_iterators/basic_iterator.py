class NumberIterator:
    def __init__(self, start=1, end=10):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
