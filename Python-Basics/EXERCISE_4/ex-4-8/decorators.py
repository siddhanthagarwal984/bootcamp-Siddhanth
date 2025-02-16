def custom_logger(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{message} - Starting {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{message} - Finished {func.__name__}")
            return result
        return wrapper
    return decorator
