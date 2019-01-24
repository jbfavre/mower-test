#def get_next_position(new_x, new_y, orientation):
#    """ Compute next mower position
#
#    This method computes next theoretical mower's position.
#    The new position is theoric because it's not validated
#    Validation will happen in check_next_position which is
#    called from move_mower.
#
#    Parameters:
#        new_x (int): mower's current horizontal coordinate
#        new_y (int): mower's current vertical coordinate
#        orientation (str): mower's orientation. Must be one of [N, E, S, W]
#    Returns:
#        new_x (str): mower's new horizontal coordinate
#        new_y (str): mower's new vertical coordinate
#    """
#
#    if orientation == "N":
#        new_y = new_y + 1
#    elif orientation == "E":
#        new_x = new_x + 1
#    elif orientation == "S":
#        new_y = new_y - 1
#    elif orientation == "W":
#        new_x = new_x - 1
#    else:
#        raise ValueError(
#            "Invalid orientation. Got %s, expected one of [N, E, S, W]" % orientation
#        )
#
#    return str(new_x), str(new_y)

import pytest

from mower import get_next_position

def test_get_next_position():
    data = [
        (0, 0, "N", ('0', '1')),
        (5, 5, "W", ('4', '5'))
    ]
    for arguments in data:
        pos_x, pos_y, orientation, expected_result = arguments
        new_x, new_y = get_next_position(pos_x, pos_y, orientation)
        assert (new_x, new_y) == expected_result

def test_get_next_position_invalid():
    data = [
        (0, 0, "A")
    ]
    for arguments in data:
        pos_x, pos_y, orientation = arguments
        with pytest.raises(ValueError) as err:
            get_next_position(pos_x, pos_y, orientation)
        assert str(err.value) == "Invalid orientation. Got %s, expected one of [N, E, S, W]" % orientation
