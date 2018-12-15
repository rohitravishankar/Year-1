__author__ = 'Rohit Ravishankar'
__email__ = "rr9105@rit.edu"

from utils import *
from route_finder import *


def main():
    """
    Main calling program for the code
    :return: None
    """
    # To get all the necessary files
    terrain_map, modified_elevation_matrix, classic_courses, scoreo_course = get_files()

    # To find the routing for the classic routes
    classic_route(terrain_map, modified_elevation_matrix, classic_courses)

    # To find the routing for score-o route
    scoreo_route(terrain_map, modified_elevation_matrix, scoreo_course)

    # To move the output map files to the Output folder
    move_output_files()


if __name__ == '__main__':
    main()
