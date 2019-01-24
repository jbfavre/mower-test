#def check_new_position(lawn_map, x, y):
#    """ Check new position validity
#
#    This method checks new position validity with 2 rules:
#    - next position should not be outside of the map.  
#    It tries to read next position value. If we're outside of the map,
#    this will trigger an IndexError exception
#    - next position must not be already occupied.
#    We use assertion for that, assuming next position value is None.
#    If position is already occupied by another mower, it triggers an AssertionError exception
#
#    Parameters:
#        lawn_map (list): list of lawn columns
#        x (int): mower's horizontal coordinate
#        y (int): mower's vertical coordinate
#    """
#
#    try:
#        cur_value = lawn_map[x][y]
#    except:
#        raise IndexError("check_new_position: Can not go out of the map")
#    try:
#        assert(lawn_map[x][y] is None)
#    except:
#        raise ValueError("check_new_position: Position already occupied by another mower")

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
