import pytest

def test_01():
    assert 1 == 1

def test_02():
    assert  11 == 23

if __name__ == "__main__":
    pytest.main(["-s", "test_python.py"])
