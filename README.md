# Student Study & Marks Management System

## Overview
A Python-based console application for managing student records, entering marks, calculating results, and generating reports.

## Features
- Add, search, list and delete students
- Add/update subject marks
- Calculate total, percentage, grade and pass/fail status
- Generate a text result report
- JSON-based persistent storage
- Input validation and error handling
- Automated validation tests

## Technologies
- Python 3
- JSON
- Git/GitHub
- Python unittest/pytest-compatible assertions

## Project Structure
```text
student_management_system/
├── main.py
├── student.py
├── marks.py
├── result.py
├── report.py
├── storage.py
├── validation.py
├── data/students.json
├── tests/test_project.py
├── docs/
├── README.md
└── statement.md
```

## How to Run
1. Install Python 3.
2. Download/clone the repository.
3. Open the project folder in a terminal.
4. Run:
```bash
python main.py
```

## Testing
Run:
```bash
python -m pytest
```
If pytest is not installed, the individual functions can also be tested using Python's standard tools or an IDE test runner.

## Input/Output
Input: student roll number, name, branch, subject names and marks (0-100).
Output: student records, calculated result and generated report file.

## Academic Relevance
The project demonstrates Python variables, data types, conditional statements, loops, functions, modules, dictionaries, lists, file handling, exception handling and validation.

## Version Control
The project is designed to be maintained in a Git repository and submitted as a GitHub repository.
