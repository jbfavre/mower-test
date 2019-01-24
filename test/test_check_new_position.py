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
    EMPTY_MAP = []
    for i in range(12):
        EMPTY_MAP.append([None] * 15)
    return EMPTY_MAP

def test_check_new_position():
    NEW_POSITION = [
        (0, 0),
        (4, 2),
        (5, 7)
    ]
    for POSITION in NEW_POSITION:
        x, y = POSITION
        check_new_position(generate_empty_map(), x, y)

def test_check_new_position_invalid_outside_map():
    NEW_POSITION = [
        (21, 2),
        (1, 22),
        (21, 22)
    ]
    for POSITION in NEW_POSITION:
        x, y = POSITION
        with pytest.raises(IndexError) as err:
            check_new_position(generate_empty_map(), x, y)
        assert str(err.value) == 'check_new_position: Can not go out of the map'

def test_check_new_position_invalid():
    MAP = [
        [None, 1, None],
        [None, None, None],
    ]
    with pytest.raises(ValueError) as err:
        check_new_position(MAP, 0, 1)
    assert str(err.value) == 'check_new_position: Position already occupied by another mower'
