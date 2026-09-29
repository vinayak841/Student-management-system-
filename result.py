from storage import load_data

def grade(percentage):
    if percentage >= 90: return "A+"
    if percentage >= 80: return "A"
    if percentage >= 70: return "B"
    if percentage >= 60: return "C"
    if percentage >= 50: return "D"
    if percentage >= 40: return "E"
    return "F"

def calculate_result():
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
    print(f"\nStudent: {student['name']}")
    print(f"Total: {total:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade(percentage)}")
    print(f"Status: {status}")
