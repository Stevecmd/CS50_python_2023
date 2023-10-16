from plates import is_valid
import pytest
import sys # I am using it to exit but its not necessary for the program to run

def main():
    test_basic_validity(),
    test_length_restrictions(),
    test_starting_characters(),
    test_invalid_characters(),
    test_number_positioning(),
    test_initial_zero()

def test_basic_validity():
    assert is_valid("AB1234") == True
    assert is_valid("AB12") == True
    assert is_valid("ABCD") == True

def test_length_restrictions():
    assert is_valid("A") == False  # License plate is too short
    assert is_valid("ABCDEFG") == False  # License plate is too long

def test_starting_characters():
    assert is_valid("1BCD") == False  # License plate does not start with two letters
    assert is_valid("A1CD") == False  # License plate does not start with two letters
    assert is_valid(" 1234") == False  # License plate has space at the beginning, does not start with two letters
    assert is_valid("1234") == False    # License plate does not start with two letters, check for numbers

def test_invalid_characters():
    assert is_valid("AB.CD") == False  # License plate contains period
    assert is_valid("AB CD") == False  # License plate contains space
    assert is_valid("AB!CD") == False  # License plate contains punctuation

def test_number_positioning():
    assert is_valid("A1BCD") == False  # Number in the middle
    assert is_valid("AB1C2") == False  # Number in the middle

def test_initial_zero():
    assert is_valid("AB0123") == False  # First number is zero

if __name__ == "__main__":
    main()
    sys.exit(1)

