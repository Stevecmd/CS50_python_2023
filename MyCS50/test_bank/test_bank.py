# implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
# and treat the user’s greeting case-insensitively.

from bank import value
import pytest

def main():
    test_correct_values()
    test_lowercase()
    test_no_Input()
    test_starts_with_h()
    test_not_start_with_h()
    test_spaces_only()
    test_case_insensitivity()

def test_correct_values():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("world") == 100

def test_case_insensitivity():
    assert value("hELLO") == 0
    assert value("hI") == 20

def test_lowercase():
    assert value("hello") == 0

def test_no_Input():
    assert value("") == 100

def test_spaces_only():
    assert value("   ") == 100

def test_starts_with_h():
    assert value("hi") == 20

def test_not_start_with_h():
    assert value("world") == 100

def test_case_insensitivity():
    assert value("HELLO") == 0
    assert value("Hello") == 0
    assert value("hELLO") == 0
    assert value("HI") == 20
    assert value("hI") == 20

if __name__ == "__main__":
    main()
