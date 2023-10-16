from calculator import square
# We are importing pytest to: Check for integers
import pytest

# def main():
#     test_square()

# # Version 1 - works but doesnt let us know what went wrong
# # def test_square():
# #     if square(2) != 4:
# #         print("2 sqaured was not 4") # Not a great test because 2 + 2 is 4 as well
# #     if square(3) != 9:
# #         print("3 sqaured was not 9")

# # Version 2
# # def test_square():
# #     assert square(2) == 4
# #     assert square(3) == 9

# # Version 3 - Assertions and exceptions help us determine what went wrong
# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared was not 0")

# Version 4 - using pytest
# run as pytest test_calculator.py
# from calculator import square

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-4) == 16
#     assert square(-3) == 9
#     assert square(0) == 0

# if __name__ == "__main__":
#     main()

# Version 5 - using pytest
# run as pytest test_calculator.py
# in order to run all the tests past breakage point - separate

def main():
    test_positive(),
    test_negative(),
    test_zero()


def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-4) == 16
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# Check for integers
def test_str():
    with pytest.raises(TypeError):
        square("cat") # checks for cat only


if __name__ == "__main__":
    main()