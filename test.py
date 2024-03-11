from app import add, divide
import pytest

def test_add():
    assert(add(1,1), 2)

def test_divide():
     assert(divide(10,2), 5)
