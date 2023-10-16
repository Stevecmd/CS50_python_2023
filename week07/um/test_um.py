from um import count

# My tests

# Normal um
def test_basic_count():
    assert count("hello, um, world") == 1

# Um with surrounding elements
def test_punctuation_count():
    assert count("Um, thanks for the album.") == 1
    assert count("Um? Thanks? um...") == 2

# Um within a word
def test_in_word_count():
    assert count("yummy food") == 0
    assert count("aluminum metal") == 0

# No Um present
def test_no_um_count():
    assert count("hello world") == 0

# Empty string test
def test_empty_string():
    assert count("") == 0