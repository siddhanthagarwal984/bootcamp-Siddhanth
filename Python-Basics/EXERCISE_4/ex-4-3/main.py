from decorators import timer
import time

@timer
def slow_function():
    time.sleep(2)
    print("Function executed")

slow_function()
