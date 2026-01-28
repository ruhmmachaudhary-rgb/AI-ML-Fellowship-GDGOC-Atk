# decorators.py
import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.5f} seconds")
        return result
    return wrapper

# Example function

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print(add_numbers(10, 20))

