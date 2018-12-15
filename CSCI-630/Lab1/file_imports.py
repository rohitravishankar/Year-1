__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"

from PIL import Image


def import_terrain_map(file_path):
    """
    To import the map/terrain from memory
    :param file_path: Path to the image file
    :return: Object of the read image
    """
    # To read image file into memory
    terrain_map = Image.open(file_path)
    return terrain_map


def import_elevation_matrix(file_path):
    """
    To import the elevation matrix from memory
    :param file_path: Path to the elevation matrix
    :return: Object of the elevation matrix
    """
    # To read image elevation file into memory
    with open(file_path) as file:
        elevation_matrix = [[float(num) for num in line.split()] for line in file]

    return elevation_matrix


def import_classic_course(file_path):
    """
    To read the classic event - white, brown and red course file into memory
    :param file_path: Path to the file
    :return: list of controls and the starting control
    """

    # To store the start state and (list of the controls - start state)
    start = ()
    controls = []
    with open(file_path) as file:

        if "Classic" in file.readline():
            init = file.readline().split()

            # We want to store the starting coordinates
            start = (int(init[0]), int(init[1]))
            controls = []

            # To store the coordinates to the controls
            for line in file:
                line = line.split()
                controls.append((int(line[0]), int(line[1])))
    return start, controls


def import_scoreo_course(file_path):
    """
    To read the score-o event file into memory
    :param file_path: Path to the file
    :return: Allowed time, start/finish location and the list of controls
    """
    # To store the time_limit for the score-o, start/finish coordinates, and (list of controls - start/finish state)
    time_limit = 0
    start_finish_coordinates = ()
    controls = []
    with open(file_path) as file:
        if "ScoreO" in file.readline():
            
            # The second line contains the allowed time
            time_limit = int(file.readline().strip())
            
            start_finish_line = file.readline().split()

            # The start and finish locations
            start_finish_coordinates = (int(start_finish_line[0]), int(start_finish_line[1]))

            # To store the list of controls
            controls = []
            for line in file:
                line = line.split()
                controls.append((int(line[0]), int(line[1])))

    return time_limit, start_finish_coordinates, controls
