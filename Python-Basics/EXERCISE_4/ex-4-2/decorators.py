def prefix_printer(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} {func.__name__} started")
            return func(*args, **kwargs)
        return wrapper
    return decorator
