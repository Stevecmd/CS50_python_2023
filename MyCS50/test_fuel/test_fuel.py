from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("9/9") == 100
    with pytest.raises(ValueError):
        convert("10/5")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    for i in range(2, 99):
        assert gauge(i) == f'{i}%'

if __name__ == "__main__":
    pytest.main()
