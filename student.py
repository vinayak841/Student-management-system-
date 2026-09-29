from storage import load_data, save_data
from validation import valid_name, valid_roll

def add_student():
    roll = input("Roll number: ").strip()
    name = input("Name: ").strip()
    branch = input("Branch: ").strip()
    if not valid_roll(roll):
        raise ValueError("Roll number cannot be empty.")
    if not valid_name(name):
        raise ValueError("Name must contain letters and spaces only.")
    students = load_data()
    if any(s["roll_no"] == roll for s in students):
        raise ValueError("Roll number already exists.")
    students.append({"roll_no": roll, "name": name, "branch": branch, "marks": {}})
    save_data(students)
    print("Student added successfully.")

def list_students():
    students = load_data()
    if not students:
        print("No students found.")
        return
    for s in students:
        print(f'{s["roll_no"]} | {s["name"]} | {s["branch"]}')

def find_student():
    roll = input("Enter roll number: ").strip()
    student = next((s for s in load_data() if s["roll_no"] == roll), None)
    print(student if student else "Student not found.")

def delete_student():
    roll = input("Enter roll number to delete: ").strip()
    students = load_data()
    updated = [s for s in students if s["roll_no"] != roll]
    if len(updated) == len(students):
        print("Student not found.")
    else:
        save_data(updated)
        print("Student deleted.")
