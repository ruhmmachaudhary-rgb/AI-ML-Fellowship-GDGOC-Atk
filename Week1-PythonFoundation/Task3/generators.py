# generators.py

# Fibonacci generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Custom range generator
def my_range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step

# Example usage
if __name__ == "__main__":
    print("Fibonacci:")
    for num in fibonacci(5):
        print(num, end=" ")

    print("\nCustom range:")
    for num in my_range(1, 10, 2):
        print(num, end=" ")

