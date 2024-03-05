from app import add
import pytest

def test_add():
    assert(add(1,1), 2)

def test_divide(self):
    with pytest.raises(ZeroDivisionError): 
         100 / 0