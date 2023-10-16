# To run a test in a different directory
# You also have to create a file called __init__.py
# We can now run pytest on the whole folder: pytest test

from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"