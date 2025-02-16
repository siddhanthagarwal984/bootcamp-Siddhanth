def validate_args(func):
    def wrapper(self, *args, **kwargs):
        if any(arg is None for arg in args):
            raise ValueError("None values are not allowed!")
        return func(self, *args, **kwargs)
    return wrapper
