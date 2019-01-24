#def move_mower(lawn_map, mower):
#
#            new_orientation = get_next_orientation(new_orientation, move)
#            new_x, new_y = get_next_position(int(cur_x), int(cur_y), orientation)
#            check_new_position(int(new_x), int(new_y), new_orientation, lawn_map)
#
#    return lawn_map, mower
import pytest

from mower import move_mower

def generate_empty_map():
    return [[None] * 15 for num in range(12)]

def test_move_mower():
    fake_map = generate_empty_map()
    fake_map[0][0] == 1
    fake_mower = {"position": (0, 0, "E"), "movelist": "FLFFR"}
    lawn_map, mower = move_mower(fake_map, fake_mower)
    assert lawn_map[0][0] is None
    assert lawn_map[1][2] == 1
    assert mower == {"position": ('1', '2', "E"), "movelist": "FLFFR"}
