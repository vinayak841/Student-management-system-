import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))
from result import grade
from validation import valid_mark, valid_name

def test_grade():
    assert grade(95) == "A+"
    assert grade(85) == "A"
    assert grade(45) == "E"
    assert grade(30) == "F"

def test_validation():
    assert valid_mark(0)
    assert valid_mark(100)
    assert not valid_mark(101)
    assert valid_name("Hariom Mewada")
    assert not valid_name("Hariom123")
