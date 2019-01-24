"""
Tests for init_lawn method
"""
import pytest

from mower import init_mower

def generate_empty_map():
    EMPTY_MAP = []
    for i in range(12):
        EMPTY_MAP.append([None] * 15)
    return EMPTY_MAP

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
        lawn_map, mower = init_mower(FAKE_MAP, mower_initial_position, mower_moves_list)
    assert str(err.value) == 'check_new_position: Position already occupied by another mower'

def test_init_mower_invalid_neg_int():
    mower_initial_position = (-1, 3, "E")
    mower_moves_list = "LFLFLFLFF"
    with pytest.raises(ValueError) as err:
        lawn_map, mower = init_mower(generate_empty_map(), mower_initial_position, mower_moves_list)
    assert str(err.value) == 'Both params must be greater or equal to zero'

def test_init_mower_invalid_int_neg():
    mower_initial_position = (1, -3, "E")
    mower_moves_list = "LFLFLFLFF"
    with pytest.raises(ValueError) as err:
        lawn_map, mower = init_mower(generate_empty_map(), mower_initial_position, mower_moves_list)
    assert str(err.value) == 'Both params must be greater or equal to zero'

def test_init_mower_position_invalid_orientation():
    mower_initial_position = (2, 2, "F")
    mower_moves_list = "LFLFLFLFF"
    with pytest.raises(ValueError) as err:
        lawn_map, mower = init_mower(generate_empty_map(), mower_initial_position, mower_moves_list)
    assert str(err.value) == 'Invalid orientation. Expected one of [NESW], got F'

def test_init_mower_position_invalid_out_of_map():
    mower_initial_position = (22, 22, "E")
    mower_moves_list = "LFLFLFLFF"
    with pytest.raises(IndexError) as err:
        lawn_map, mower = init_mower(generate_empty_map(), mower_initial_position, mower_moves_list)
    assert str(err.value) == 'check_new_position: Can not go out of the map'
