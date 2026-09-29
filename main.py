from student import add_student, list_students, find_student, delete_student
from marks import add_marks
from result import calculate_result
from report import generate_report

def menu():
    print("\n=== Student Study & Marks Management System ===")
    print("1. Add student")
    print("2. List students")
    print("3. Search student")
    print("4. Add/update marks")
    print("5. View result")
    print("6. Generate report")
    print("7. Delete student")
    print("0. Exit")

def run():
    while True:
        menu()
        choice = input("Enter choice: ").strip()
        try:
            if choice == "1":
                add_student()
            elif choice == "2":
                list_students()
            elif choice == "3":
                find_student()
            elif choice == "4":
                add_marks()
            elif choice == "5":
                calculate_result()
            elif choice == "6":
                generate_report()
            elif choice == "7":
                delete_student()
            elif choice == "0":
                print("Thank you!")
                break
            else:
                print("Invalid choice.")
        except (ValueError, KeyError) as exc:
            print(f"Error: {exc}")

if __name__ == "__main__":
    run()
