import pytest

from mower import check_new_position

def generate_empty_map():
    return [[None] * 15 for num in range(12)]

def test_check_new_position():
    NEW_POSITION = [
        (0, 0, "N", generate_empty_map()),
        (4, 2, "E", generate_empty_map()),
        (5, 7, "S", None)
    ]
    for POSITION in NEW_POSITION:
        pos_x, pos_y, pos_o, map = POSITION
        check_new_position(pos_x, pos_y, pos_o, map)

def test_check_new_position_invalid_outside_map():
    NEW_POSITION = [
        (21, 2, "N", generate_empty_map()),
        (1, 22, "E", generate_empty_map()),
        (21, 22, "S", generate_empty_map()),
    ]
    for POSITION in NEW_POSITION:
        x, y, pos_o, map = POSITION
        with pytest.raises(IndexError) as err:
            check_new_position(x, y, pos_o, map)
        assert str(err.value) == 'Can not go out of the map'

def test_check_new_position_invalid():
    MAP = [
        [None, 1, None],
        [None, None, None],
    ]
    with pytest.raises(ValueError) as err:
        check_new_position(0, 1, "N", MAP)
    assert str(err.value) == 'Position already occupied by another mower'

def test_check_new_position_invalid_orientation():
    NEW_POSITION = [
        (2, 2, "A", generate_empty_map()),
        (1, 10, "F", generate_empty_map()),
        (9, 5, "G", None),
    ]
    for POSITION in NEW_POSITION:
        pos_x, pos_y, pos_o, map = POSITION
        with pytest.raises(ValueError) as err:
            check_new_position(pos_x, pos_y, pos_o, map)
        assert str(err.value) == 'Invalid orientation. Got %s, expected one of [N, E, S, W]' % pos_o
