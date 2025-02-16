import time

def retry(attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i+1} failed: {e}")
                    time.sleep(delay)
            print("All retries failed.")
        return wrapper
    return decorator
