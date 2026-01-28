# data_op.py

def remove_duplicates(lst):
    return list(set(lst))

def find_max(lst):
    return max(lst)

def find_min(lst):
    return min(lst)

# Example
if __name__ == "__main__":
    data = [5, 3, 8, 3, 9]
    print("Unique:", remove_duplicates(data))
    print("Max:", find_max(data))
    print("Min:", find_min(data))

