from storage import load_data
from result import grade

def generate_report():
    roll = input("Roll number: ").strip()
    student = next((s for s in load_data() if s["roll_no"] == roll), None)
    if not student:
        print("Student not found.")
        return
    marks = student["marks"]
    if not marks:
        print("No marks available.")
        return
    total = sum(marks.values())
    percentage = total / len(marks)
    status = "PASS" if all(m >= 40 for m in marks.values()) else "FAIL"
    filename = f"report_{roll}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write("STUDENT RESULT REPORT\n")
        file.write("=" * 30 + "\n")
        file.write(f"Roll No: {roll}\nName: {student['name']}\nBranch: {student['branch']}\n\n")
        for subject, mark in marks.items():
            file.write(f"{subject}: {mark}\n")
        file.write(f"\nPercentage: {percentage:.2f}%\nGrade: {grade(percentage)}\nStatus: {status}\n")
    print(f"Report generated: {filename}")
