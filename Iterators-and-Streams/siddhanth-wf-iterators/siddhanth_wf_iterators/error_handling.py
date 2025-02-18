def safe_file_generator(filename, keyword):
    try:
        with open(filename, "r") as file:
            for line in file:
                if keyword in line:
                    yield line.strip()
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
