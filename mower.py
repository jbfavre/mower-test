#/usr/bin/env python3
""" Tech test for BlaBlaCar hiring process

The script implement an undefined number of automatic mowers
"""

__VERSION__ = '0.1'

import argparse
import logging
try:
    from itertools import zip_longest
except ImportError:
    from itertools import izip_longest as zip_longest

def read_args():
    """ Read command line arguments

    Reads and return command line arguments & values
    """

    description = 'Mower command line switches'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-f", "--file", help="File with move instructions", required=True)
    parser.add_argument(
        "-d", "--debug", help="Enable debug logging", dest='debug', action='store_true')
    return parser.parse_args()

def init_lawn(horizontal, vertical):
    """ Initialize lawn map

    This function simply creates a list of list
    using first line from input file.
    Each position is initialized with None value, meaning map is empty

    Parameters:
        horizontal (int): horizontal size of the lawn
        vertical   (int): vertical size of the lawn
    Returns:
        lawn: list of lawn columns
    """

    # Doesn't seem to work. Create somehow linked copies of fir list
    # which breaks position updates later
    # lawn = [[None] * vertical] * horizontal

    # Create empty map[X][Y]
    # X: horizontal index
    # Y: vertical index
    if not isinstance(horizontal, int) or not isinstance(horizontal, int):
        raise TypeError("Both parmas must be integer")
    if not horizontal >= 0 or not vertical >= 0:
        raise ValueError("Both params must be greater or equal to zero")

    lawn = [[None] * vertical for num in range(horizontal)]

    return lawn

def init_mower(lawn_map, mower_initial_position, mower_moves_list):
    """ Initialize new mower

    This method is used to create a mower
    It checks that new position is valid, update lawn_map
    and returns both lawn_map & mower.

    Parameters:
        lawn_map (list): list of lawn columns
        mower_initial_position (tuple): mower's horizontal & vertical coordinates,
            mower's orientation
        mower_moves_list (str): mower's moves to process
    Returns:
        lawn_map (list): list of lawn columns
        mower (dict): mower's position & moves list
    """

    pos_x = int(mower_initial_position[0])
    pos_y = int(mower_initial_position[1])
    pos_o = mower_initial_position[2]

    try:
        # Initialize mower and mark its position occupied on the map
        # only if position isn't already filled
        check_new_position(pos_x, pos_y, pos_o, lawn_map)
    except ValueError as err:
        # mower next position is already occupied.
        raise err
    except IndexError as err:
        # mower tries to go out of the map
        raise err

    # Initialize mower
    mower = {"position": mower_initial_position, "movelist": mower_moves_list}
    # Mark mower's position occupied on the map
    lawn_map[pos_x][pos_y] = 1

    return lawn_map, mower

def check_new_position(pos_x, pos_y, pos_o, lawn_map=None):
    """ Check new position validity

    This method checks new position validity with 2 rules:
    - next position should not be outside of the map.
    It tries to read next position value. If we're outside of the map,
    this will trigger an IndexError exception
    - next position must not be already occupied.
    We use assertion for that, assuming next position value is None.
    If position is already occupied by another mower, it triggers an
        AssertionError exception

    Parameters:
        lawn_map (list): list of lawn columns
        pos_x (int): mower's horizontal coordinate
        pos_y (int): mower's vertical coordinate
    """

    if not isinstance(pos_x, int) or not isinstance(pos_y, int):
        raise TypeError("Both parmas must be integer")
    if pos_x < 0 or pos_y < 0:
        raise ValueError("Both params must be greater or equal to zero")
    if pos_o not in "NESW":
        raise ValueError(
            "Invalid orientation. Got %s, expected one of [N, E, S, W]" % pos_o
        )
    if lawn_map is not None:
        try:
            lawn_map[pos_x][pos_y]
        except:
            raise IndexError("Can not go out of the map")
        try:
            assert lawn_map[pos_x][pos_y] is None
        except:
            raise ValueError("Position already occupied by another mower")

def get_next_orientation(orientation, move):
    """ Compute next mower orientation

    2 moves are allowed: Left or Right
    Given an orientation, get corresponding index from orientation's list
    Add (move is Right) or remove (move is Left) 1 from this index,
    and get the new orientation letter based on the index.
    We use modulo so handle move from West to North, and North to West

    Parameters:
        orientation (str): mower's orientation. Must be one of [N, E, S, W]
        move (str): mower's wanted move. Must be one of [L, R]
    Returns:
        orientation (str): new mower's orientation. Must be one of [N, E, S, W]
    """

    orientation_list = "NESW"
    try:
        orientation_index = orientation_list.index(orientation)
    except ValueError:
        raise ValueError(
            "Invalid orientation. Got %s, expected one of [N, E, S, W]" % orientation
        )
    new_orientation_index = orientation_index
    if move == "L":
        new_orientation_index = orientation_index - 1
    if move == "R":
        new_orientation_index = orientation_index + 1

    return orientation_list[new_orientation_index % len(orientation_list)]

def get_next_position(new_x, new_y, orientation):
    """ Compute next mower position

    This method computes next theoretical mower's position.
    The new position is theoric because it's not validated
    Validation will happen in check_next_position which is
    called from move_mower.

    Parameters:
        new_x (int): mower's current horizontal coordinate
        new_y (int): mower's current vertical coordinate
        orientation (str): mower's orientation. Must be one of [N, E, S, W]
    Returns:
        new_x (str): mower's new horizontal coordinate
        new_y (str): mower's new vertical coordinate
    """

    if orientation == "N":
        new_y = new_y + 1
    elif orientation == "E":
        new_x = new_x + 1
    elif orientation == "S":
        new_y = new_y - 1
    elif orientation == "W":
        new_x = new_x - 1
    else:
        raise ValueError(
            "Invalid orientation. Got %s, expected one of [N, E, S, W]" % orientation
        )

    return str(new_x), str(new_y)

def move_mower(lawn_map, mower):
    """ Compute new mower's position or orientation, update lawn_map and mower

    This function iterates on mower's movelist and update lawn_map &
    mower's position & orientation accordingly.
    It uses get_next_orientation and get_next_position to get data,
    then validate new position against check_new_position method
    It updates lawn_map & mower unless anything goes wrong.
    In this case, an excpetion is raised.

    Parameters:
        lawn_map (list): list of lawn map columns
        mower (dict): mower's attributes
    Returns:
        lawn_map (list): list of lawn map columns
        mower (dict): mower's attributes
    """

    for move in mower["movelist"]:
        cur_x, cur_y, orientation = mower["position"]
        new_x, new_y, new_orientation = mower["position"]
        if move in ["L", "R"]:
            # Updating orientation without moving
            # Get new orientation
            new_orientation = get_next_orientation(orientation, move)
        elif move in ["F"]:
            # Moving without changing orientation
            # Get new position
            # Possible error when passing bad orientation as argument
            try:
                new_x, new_y = get_next_position(int(cur_x), int(cur_y), orientation)
            except ValueError as err:
                # mower next position is already occupied.
                # Cancelling the move, but continue processing
                print(err)
                continue
            try:
                # Check that next position is valid
                # Possible error if position outside of the map
                # or position already occupied by another mower
                check_new_position(int(new_x), int(new_y), new_orientation, lawn_map)
            except (TypeError, IndexError, ValueError) as err:
                # Either position is outside the map,
                # or new position is already occupied by another mower
                # Cancel the move, but continue processing
                print(err)
                continue
            # Move succeeded. Freeing old map location
            lawn_map[int(new_x)][int(new_y)] = 1
            lawn_map[int(cur_x)][int(cur_y)] = None
        else:
            raise ValueError("Invalid move command. Got %s, expected one of [L, R, F]" % move)
        # Check new position
        # Possibly get IndexError when trying to go outside of the map
        #              ValueError if next location is already occupied by another mower
        logging.debug(
            "Current position: %s. Next position: %s after move %s)",
            mower["position"], (str(new_x), str(new_y), new_orientation), move
        )
        mower["position"] = (new_x, new_y, new_orientation)
    logging.debug("Final   position: %s", str(mower["position"]))

    return lawn_map, mower

def main():
    """ Read input file and process informations

    It initialize lawn map and iterate on mower's to create them,
    place them on the map and process moves.

    First line from input file is lawn map size
    Others lines are grouped 2 by 2 and mean:
    - mower's initial position & orientation
    - mower's moves list

    Before exit, mowers' status is displayed
    """

    # Process command line arguments and setup logging verbosity
    args = read_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    with open(args.file) as input_file:
        # First line is lawn size
        (lawn_size_horizontal, lawn_size_vertical) = tuple(
            int(x) for x in input_file.readline().rstrip().split(" ")
        )
        lawn_map = init_lawn(lawn_size_horizontal+1, lawn_size_vertical+1)

        # Next lines are grouped 2 by 2 which define:
        # - mower initial position & orientation
        # - mower moves list
        mowers = 0
        for initial_position, moves_list in zip_longest(*[input_file]*2):
            mowers += 1
            if moves_list is None:
                # If we don't have enough lines for current mower
                # That means we reached the end of the line
                # Therefore, we can safely exit loop
                logging.debug("Not enough line. Skipping mower")
                break
            logging.debug("Initializing mower")
            # Extract moxer's position, orientation and moves' list from input file
            mower_initial_position = tuple(x for x in initial_position.rstrip().split(" "))
            mower_moves_list = moves_list.replace(" ", "").rstrip()
            try:
                # Initialize mower
                lawn_map, mower = init_mower(lawn_map, mower_initial_position, mower_moves_list)
            except ValueError as err:
                print("Mower %d: %s" % (mowers, err))
                continue
            except IndexError as err:
                print("Mower %d: %s" % (mowers, err))
                continue
            logging.debug("Mower %d created", mowers)
            try:
                lawn_map, mower = move_mower(lawn_map, mower)
            except ValueError as err:
                print("Mower %d: %s" % (mowers, err))
                continue
            # Mower's moves' list processed.
            # Print final mower's position & orientation
            print(" ".join(mower["position"]))

if __name__ == '__main__':
    main()
