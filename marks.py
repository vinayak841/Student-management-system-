from storage import load_data, save_data
from validation import valid_mark

def add_marks():
    roll = input("Roll number: ").strip()
    students = load_data()
    student = next((s for s in students if s["roll_no"] == roll), None)
    if not student:
        raise ValueError("Student not found.")
    print("Enter marks. Type 'done' when finished.")
    while True:
        subject = input("Subject: ").strip()
        if subject.lower() == "done":
            break
        if not subject:
            print("Subject cannot be empty.")
            continue
        mark = float(input(f"Marks for {subject}: "))
        if not valid_mark(mark):
            raise ValueError("Marks must be between 0 and 100.")
        student["marks"][subject] = mark
    save_data(students)
    print("Marks saved.")
