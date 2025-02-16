from decorators import custom_logger

@custom_logger("DEBUG")
def process_data():
    print("Processing data...")

process_data()
