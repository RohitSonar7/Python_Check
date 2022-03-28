import Check
import pytest

@pytest.fixture()
def input():
    a = 25
    return a

def test_By5_1(input):

    result = Check.By5(input)
    assert result == True

def test_By5_2(input):

    result = Check.By5(input)
    assert result == False

def test_By7_1(input):

    result = Check.By7(input)
    assert result == True

def test_By7_2(input):

    result = Check.By7(input)
    assert result == False
def test_By9_1(input):

    result = Check.By9(input)
    assert result == True

def test_By9_2(input):

    result = Check.By9(input)
    assert result == False

def test_By11_1(input):

    result = Check.By11(input)
    assert result == True

def test_By11_2(input):

    result = Check.By11(input)
    assert result == False






