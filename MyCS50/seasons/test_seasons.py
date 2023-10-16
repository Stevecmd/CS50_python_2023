import pytest
from seasons import minutes_since_birth, number_to_words
from datetime import date

def test_minutes_since_birth():
    assert minutes_since_birth(date(2000, 1, 1)) == ((date.today() - date(2000, 1, 1)).days * 24 * 60)

def test_number_to_words():
    assert number_to_words(365) == 'Three hundred sixty-five'
    assert number_to_words(2000) == 'Two thousand'
    assert number_to_words(14567) == 'Fourteen thousand, five hundred sixty-seven'
