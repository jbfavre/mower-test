#def get_next_orientation(orientation, move):
#    """ Compute next mower orientation
#
#    2 moves are allowed: Left or Right
#    Given an orientation, get corresponding index from orientation's list
#    Add (move is Right) or remove (move is Left) 1 from this index,
#    and get the new orientation letter based on the index.
#    We use modulo so handle move from West to North, and North to West
#
#    Parameters:
#        orientation (str): mower's orientation. Must be one of [N, E, S, W]
#        move (str): mower's wanted move. Must be one of [L, R]
#    Returns:
#        orientation (str): new mower's orientation. Must be one of [N, E, S, W]
#    """
#
#    orientation_list = "NESW"
#    orientation_index = orientation_list.index(orientation)
#    if move == "L":
#        offset = int(orientation_index - 1)
#    if move == "R":
#        offset = int(orientation_index + 1)
#
#    return orientation_list[(len(orientation_list) + offset) % len(orientation_list)]

import pytest

from mower import get_next_orientation

def test_get_next_orientation():
    data = [
        ("N", "L", "W"),
        ("E", "R", "S")
    ]
    for arguments in data:
        orientation, move, expected_result = arguments
        new_orientation = get_next_orientation(orientation, move)
        assert new_orientation == expected_result

def test_get_next_orientation_invalid_move():
    data = [
        ("N", "A", "N")
    ]
    for arguments in data:
        orientation, move, expected_result = arguments
        new_orientation = get_next_orientation(orientation, move)
        assert new_orientation == expected_result

def test_get_next_orientation_invalid_orientation():
    data = [
        ("A", "L"),
        ("B", "R")
    ]
    for arguments in data:
        orientation, move = arguments
        with pytest.raises(ValueError) as err:
            get_next_orientation(orientation, move)
        assert str(err.value) == 'Invalid orientation. Got %s, expected one of [N, E, S, W]' % orientation
