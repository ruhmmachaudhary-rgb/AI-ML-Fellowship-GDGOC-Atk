# contact_manager.py

def add_contact(name, phone):
    with open("contacts.txt", "a") as f:
        f.write(f"{name},{phone}\n")

def view_contacts():
    with open("contacts.txt", "r") as f:
        for line in f:
            name, phone = line.strip().split(",")
            print(f"Name: {name}, Phone: {phone}")

# Example usage
if __name__ == "__main__":
    add_contact("Ali", "12345")
    view_contacts()

