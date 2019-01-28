"""
Tests for init_lawn method
"""
import pytest

from mower import init_lawn

def test_init_lawn():
    lawn_map = init_lawn(12,15)
    assert lawn_map == [[None] * 15] * 12

def test_init_lawn_invalid_int_neg():
    with pytest.raises(ValueError) as err:
        lawn_map = init_lawn(5,-1)
    assert str(err.value) == 'Both params must be greater or equal to zero'

def test_init_lawn_invalid_neg_str():
    with pytest.raises(ValueError) as err:
        lawn_map = init_lawn(-1,"A")
    assert str(err.value) == 'Both params must be greater or equal to zero'

def test_init_lawn_invalid_str_neg():
    with pytest.raises(TypeError) as err:
        lawn_map = init_lawn("A", -1)
    assert str(err.value) == 'Both parmas must be integer'
