from hello import hello

# Solution 1
# def test_hello():
#     assert hello("Steve") == "hello, Steve"
#     assert hello() == "hello, world"

# Solution 2
# def test_default():
#     assert hello() == "hello, world"

# def test_argument():
#     assert hello("Steve") == "hello, Steve"

# Solution 2
def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Harry", "Ron", "Hermione"]:
        assert hello(name) == f"hello, {name}"