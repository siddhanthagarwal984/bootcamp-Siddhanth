def file_generator(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()
