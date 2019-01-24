"""
Tests for init_lawn method
"""
import pytest

from mower import init_mower

def generate_empty_map():
    return [[None] * 15 for num in range(12)]

def test_init_mower():
    mower_initial_position = (1, 3, "E")
    mower_moves_list = "LFLFLFLFF"
    lawn_map, mower = init_mower(generate_empty_map(), mower_initial_position, mower_moves_list)
    assert lawn_map[1][3] == 1
    assert mower == {"position": (1, 3, "E"), "movelist":"LFLFLFLFF"}

def test_init_mower_position_assigned():
    mower_initial_position = (1, 3, "S")
    mower_moves_list = "LFLFLFLFF"
    FAKE_MAP = generate_empty_map()
    FAKE_MAP[1][3] = 1
    with pytest.raises(ValueError) as err:
        init_mower(FAKE_MAP, mower_initial_position, mower_moves_list)
    assert str(err.value) == 'Position already occupied by another mower'

def test_init_mower_invalid_neg_int():
    mower_initial_position = (-1, 3, "E")
    mower_moves_list = "LFLFLFLFF"
    with pytest.raises(ValueError) as err:
        init_mower(generate_empty_map(), mower_initial_position, mower_moves_list)
    assert str(err.value) == 'Both params must be greater or equal to zero'

def test_init_mower_invalid_int_neg():
    mower_initial_position = (1, -3, "E")
    mower_moves_list = "LFLFLFLFF"
    with pytest.raises(ValueError) as err:
        init_mower(generate_empty_map(), mower_initial_position, mower_moves_list)
    assert str(err.value) == 'Both params must be greater or equal to zero'

def test_init_mower_position_invalid_orientation():
    mower_initial_position = (2, 2, "F")
    mower_moves_list = "LFLFLFLFF"
    with pytest.raises(ValueError) as err:
        init_mower(generate_empty_map(), mower_initial_position, mower_moves_list)
    assert str(err.value) == 'Invalid orientation. Got F, expected one of [N, E, S, W]'

def test_init_mower_position_invalid_out_of_map():
    mower_initial_position = (22, 22, "E")
    mower_moves_list = "LFLFLFLFF"
    with pytest.raises(IndexError) as err:
        init_mower(generate_empty_map(), mower_initial_position, mower_moves_list)
    assert str(err.value) == 'Can not go out of the map'
