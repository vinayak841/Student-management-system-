import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "students.json"

def load_data():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)

def save_data(students):
    DATA_FILE.parent.mkdir(exist_ok=True)
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=2)

def get_student(roll_no):
    return next((s for s in load_data() if s["roll_no"] == roll_no), None)
