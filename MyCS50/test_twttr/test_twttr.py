from twttr import shorten
import pytest

def main():
    test_lowercase(),
    test_uppercase(),
    test_no_Input(),
    test_numbers_only(),
    test_punctuation()

def test_lowercase():
    assert shorten("aebght") == "bght"

def test_uppercase():
    assert shorten("AEIOUBGHT") == "BGHT"

def test_no_Input():
    assert shorten("") == ""

def test_numbers_only():
    assert shorten("123") == "123"

def test_punctuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"

if __name__ == "__main__":
    main()