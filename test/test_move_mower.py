#def move_mower(lawn_map, mower):
#
#            new_orientation = get_next_orientation(new_orientation, move)
#            new_x, new_y = get_next_position(int(cur_x), int(cur_y), orientation)
#            check_new_position(int(new_x), int(new_y), new_orientation, lawn_map)
#
#    return lawn_map, mower
import pytest
import mock
from mower import move_mower

def generate_empty_map():
    return [[None] * 15 for num in range(12)]

@mock.patch("mower.get_next_orientation")
@mock.patch("mower.get_next_position")
@mock.patch("mower.check_new_position")
def test_move_mower(mock_check_new_position, mock_get_next_position, mock_get_next_orientation):
    fake_map = generate_empty_map()
    fake_map[0][0] == 1
    fake_mower = {"position": (0, 0, "E"), "movelist": "FLFFR"}

    mock_get_next_orientation.side_effect = ["N", "E"]
    mock_get_next_position.side_effect = [(1, 0), (1, 1), (1, 2)]
    mock_check_new_position.side_effect = [None, None, None]
    with mock_get_next_orientation, mock_get_next_position, mock_check_new_position:
        test_lawn_map, test_mower = move_mower(fake_map, fake_mower)
    assert test_lawn_map[0][0] is None
    assert test_lawn_map[1][2] == 1
    assert test_mower == {"position": (1, 2, "E"), "movelist": "FLFFR"}
