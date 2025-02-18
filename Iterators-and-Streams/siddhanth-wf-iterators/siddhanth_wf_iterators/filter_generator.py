def filtered_file_generator(filename, keyword):
    with open(filename, "r") as file:
        for line in file:
            if keyword in line:
                yield line.strip()
