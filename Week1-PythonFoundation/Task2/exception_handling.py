# exception_handling.py

def safe_divide(a, b):
    try:
        return a / b
    except:
        return "Error: Check input or division by zero"

# Example
if __name__ == "__main__":
    print(safe_divide(10, 2))
    print(safe_divide(5, 0))

