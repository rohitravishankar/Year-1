__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"

import os
from file_imports import *

# stores the path to the program, i.e., the current file
PROGRAM_PATH = os.path.dirname(os.path.abspath(__file__))

# Stores the path to the static folder
STATIC_FILES_FOLDER = os.path.join(PROGRAM_PATH, "static")

# Stores the path to the output folder where you find all the output maps
OUTPUT_FILES_FOLDER = os.path.join(PROGRAM_PATH, "Output")


def modify_elevation_matrix(elevation_matrix):
    """
    To remove the last 5 columns from the elevation matrix
    :param elevation_matrix: The numpy array with the elevation matrix
    :return: Modified elevation matrix without the last 5 columns
    """
    modified_elevation_matrix = elevation_matrix

    # To remove the last 5 columns of the elevation matrix
    for i in range(5):
        for row in modified_elevation_matrix:
            del row[-1]

    return modified_elevation_matrix


def get_files():
    """
    Function to get all the files
    :return: Terrain map, Elevation matrix, White Route, Brown Route & Red Route
    """
    # To read the terrain map
    terrain_map = import_terrain_map(os.path.join(STATIC_FILES_FOLDER, "terrain.png"))

    # To read the elevation matrix
    elevation_matrix = import_elevation_matrix(os.path.join(STATIC_FILES_FOLDER, "mpp.txt"))

    # To remove the last 5 rows of the elevation matrix
    modified_elevation_matrix = modify_elevation_matrix(elevation_matrix)

    # To read the different classic trails
    white_course = import_classic_course(os.path.join(STATIC_FILES_FOLDER, "white.txt"))
    brown_course = import_classic_course(os.path.join(STATIC_FILES_FOLDER, "brown.txt"))
    red_course = import_classic_course(os.path.join(STATIC_FILES_FOLDER, "red.txt"))

    # To read the score-o course
    scoreo_course = import_scoreo_course(os.path.join(STATIC_FILES_FOLDER, "scoreo.txt"))

    return terrain_map, modified_elevation_matrix, [white_course, brown_course, red_course], scoreo_course


def move_output_files():
    """
    To move all the map file to an output folder
    :return: None
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(OUTPUT_FILES_FOLDER):
        os.makedirs(OUTPUT_FILES_FOLDER)

    # Move the map files to the Output folder
    os.rename(os.path.join(PROGRAM_PATH, "map_WHITE.png"), os.path.join(OUTPUT_FILES_FOLDER, "map_WHITE.png"))
    os.rename(os.path.join(PROGRAM_PATH, "map_BROWN.png"), os.path.join(OUTPUT_FILES_FOLDER, "map_BROWN.png"))
    os.rename(os.path.join(PROGRAM_PATH, "map_RED.png"), os.path.join(OUTPUT_FILES_FOLDER, "map_RED.png"))
    os.rename(os.path.join(PROGRAM_PATH, "map_SCORE-O.png"), os.path.join(OUTPUT_FILES_FOLDER, "map_SCORE-O.png"))
