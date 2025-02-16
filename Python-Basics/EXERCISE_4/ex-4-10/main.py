from decorators import simple_logger, timer, debug_info

@simple_logger
@timer
@debug_info
def example_function(x, y):
    time.sleep(1)
    return x + y

example_function(5, 3)
