# student_records.py

students = []

def add_student(name, age):
    students.append({"name": name, "age": age})

def display_students():
    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}")

# Example
# calling metods
if __name__ == "__main__":
    add_student("Sara", 15)
    add_student("Ali", 16)
    display_students()

