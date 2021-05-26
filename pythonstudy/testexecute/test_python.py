import pytest

def test_01():
    assert 1 == 1

def test_02():
    assert  11 == 23

def test_03():
    assert 'HelloWorld' == 'HelloWorld'

if __name__ == "__main__":
    pytest.main(["-s", "test_python.py"])
