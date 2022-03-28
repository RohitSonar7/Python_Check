import Check
import pytest

def test_By5_1():
    x = 10
    result = Check.By5(x)
    assert result == True

def test_By5_2():
    x = 12
    result = Check.By5(x)
    assert result == False

def test_By7_1():
    x = 14
    result = Check.By7(x)
    assert result == True

def test_By7_2():
    x = 11
    result = Check.By7(x)
    assert result == False
def test_By9_1():
    x = 18
    result = Check.By9(x)
    assert result == True

def test_By9_2():
    x = 10
    result = Check.By9(x)
    assert result == False

def test_By11_1():
    x = 22
    result = Check.By11(x)
    assert result == True

def test_By11_2():
    x = 10
    result = Check.By11(x)
    assert result == False






