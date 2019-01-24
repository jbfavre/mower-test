"""
Tests for init_lawn method
"""
import pytest
import mock
from mower import init_mower

def generate_empty_map():
    return [[None] * 15 for num in range(12)]

@mock.patch("mower.check_new_position")
def test_init_mower(mock_check_new_position):
    mower_initial_position = (1, 3, "E")
    mower_moves_list = "LFLFLFLFF"
    empty_map = generate_empty_map()

    with mock_check_new_position:
        mock_check_new_position.return_value = None
        lawn_map, mower = init_mower(empty_map, mower_initial_position, mower_moves_list)
    mock_check_new_position.assert_called_with(1, 3, "E", empty_map)
    assert lawn_map[1][3] == 1
    assert mower == {"position": (1, 3, "E"), "movelist":"LFLFLFLFF"}

@mock.patch("mower.check_new_position")
def test_init_mower_position_assigned(mock_check_new_position):
    mower_initial_position = (1, 3, "S")
    mower_moves_list = "LFLFLFLFF"
    fake_map = generate_empty_map()
    fake_map[1][3] = 1

    with mock_check_new_position:
        mock_check_new_position.side_effect = ValueError("Position already occupied by another mower")
        with pytest.raises(ValueError) as err:
            init_mower(fake_map, mower_initial_position, mower_moves_list)
        mock_check_new_position.assert_called_with(1, 3, "S", fake_map)
        assert str(err.value) == 'Position already occupied by another mower'

@mock.patch("mower.check_new_position")
def test_init_mower_invalid_neg_int(mock_check_new_position):
    mower_initial_position = (-1, 3, "E")
    mower_moves_list = "LFLFLFLFF"
    empty_map = generate_empty_map()

    with mock_check_new_position:
        mock_check_new_position.side_effect = ValueError("Both params must be greater or equal to zero")
        with pytest.raises(ValueError) as err:
            init_mower(empty_map, mower_initial_position, mower_moves_list)
        mock_check_new_position.assert_called_with(-1, 3, "E", empty_map)
        assert str(err.value) == 'Both params must be greater or equal to zero'

@mock.patch("mower.check_new_position")
def test_init_mower_invalid_int_neg(mock_check_new_position):
    mower_initial_position = (1, -3, "E")
    mower_moves_list = "LFLFLFLFF"
    empty_map = generate_empty_map()

    with mock_check_new_position:
        mock_check_new_position.side_effect = ValueError("Both params must be greater or equal to zero")
        with pytest.raises(ValueError) as err:
            init_mower(empty_map, mower_initial_position, mower_moves_list)
        mock_check_new_position.assert_called_with(1, -3, "E", empty_map)
        assert str(err.value) == 'Both params must be greater or equal to zero'

@mock.patch("mower.check_new_position")
def test_init_mower_position_invalid_orientation(mock_check_new_position):
    mower_initial_position = (2, 2, "F")
    mower_moves_list = "LFLFLFLFF"
    empty_map = generate_empty_map()

    with mock_check_new_position:
        mock_check_new_position.side_effect = ValueError("Invalid orientation. Got F, expected one of [N, E, S, W]")
        with pytest.raises(ValueError) as err:
            init_mower(empty_map, mower_initial_position, mower_moves_list)
        mock_check_new_position.assert_called_with(2, 2, "F", empty_map)
        assert str(err.value) == 'Invalid orientation. Got F, expected one of [N, E, S, W]'

@mock.patch("mower.check_new_position")
def test_init_mower_position_invalid_out_of_map(mock_check_new_position):
    mower_initial_position = (22, 22, "E")
    mower_moves_list = "LFLFLFLFF"
    empty_map = generate_empty_map()

    with mock_check_new_position:
        mock_check_new_position.side_effect = IndexError("Can not go out of the map")
        with pytest.raises(IndexError) as err:
            init_mower(empty_map, mower_initial_position, mower_moves_list)
        mock_check_new_position.assert_called_with(22, 22, "E", empty_map)
        assert str(err.value) == 'Can not go out of the map'
