from decorators import retry
import random

@retry(attempts=5, delay=2)
def unstable_function():
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    print("Function succeeded!")

unstable_function()
