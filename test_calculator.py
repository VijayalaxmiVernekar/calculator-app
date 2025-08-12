import pytest
from main import add, subtract , multiply

def test_add():
    assert add(3, 2) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(5, 3) == 15
