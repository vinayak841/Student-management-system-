# System Architecture

```text
User
  |
  v
main.py (Menu / Controller)
  |
  +--> student.py ------+
  |                     |
  +--> marks.py --------+--> storage.py --> data/students.json
  |                     |
  +--> result.py -------+
  |
  +--> report.py --------> report_<roll>.txt

validation.py supports input validation across modules.
```

# Workflow
```text
Start
  -> Display Menu
  -> Select Operation
  -> Validate Input
  -> Process Data
  -> Save/Read JSON
  -> Display Result / Generate Report
  -> Return to Menu
  -> Exit
```

# Use Cases
```text
Student/User
  |-- Add Student
  |-- List/Search Student
  |-- Add Marks
  |-- View Result
  |-- Generate Report
  `-- Delete Student
```

# Sequence: View Result
```text
User -> main.py: choose View Result
main.py -> result.py: calculate_result()
result.py -> storage.py: load_data()
storage.py -> result.py: student records
result.py -> User: total/percentage/grade/status
```

# Component/Class View
```text
main.py
  |-- Student functions (student.py)
  |-- Marks functions (marks.py)
  |-- Result functions (result.py)
  |-- Report functions (report.py)
  `-- Storage functions (storage.py)

Validation functions are shared by input modules.
```

# Storage Design
Each student record is stored as:
{
  "roll_no": "101",
  "name": "Student Name",
  "branch": "AI & Bioinformatics",
  "marks": {
    "Python": 85,
    "Maths": 78
  }
}
