# This file tests the modules

from math_utils import add, subtract
from string_utils import capitalize_text, reverse_text

print("Math Operations:")
print("5 + 3 =", add(5, 3))
print("10 - 4 =", subtract(10, 4))

print("\nString Operations:")
print("Capitalize 'hello' ->", capitalize_text("hello"))
print("Reverse 'Python' ->", reverse_text("Python"))

