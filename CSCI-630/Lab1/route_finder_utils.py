__author__ = 'Rohit Ravishankar'
__email__ = "rr9105@rit.edu"

import math
from itertools import permutations

# To color the path
PATH_COLOR = (255, 0, 0, 255)

# Coordinate values for the terrain map and elevations
# Map coordinates
MAP_START_X, MAP_START_Y = 0, 0

# When we compare the adjacent pixels the current pixel must be less than 394 & 499 as 394 and 499 are index values
# to 395 and 500, i.e., the terrain map window size
MAP_END_X, MAP_END_Y = 394, 499

# Latitude and longitude values for pixel size at our elevation
LATITUDE = 10.29
LONGITUDE = 7.55

# We store the terrains and tuple in reverse order for ease of access during accessing cost
TERRAIN_PIXEL_VALUES = {
    (248, 148, 18, 255): 'OPEN_LAND',
    (255, 192, 0, 255): 'ROUGH_MEADOW',
    (255, 255, 255, 255): 'EASY_MOVEMENT_FOREST',
    (2, 208, 60, 255): 'SLOW_RUN_FOREST',
    (2, 136, 40, 255): 'WALK_FOREST',
    (5, 73, 24, 255): 'IMPASSABLE_VEGETATION',
    (0, 0, 255, 255): 'LAKE_SWAMP_MARSH',
    (71, 51, 3, 255): 'PAVED_ROAD',
    (0, 0, 0, 255): 'FOOTPATH',
    (205, 0, 101, 255): 'OUT_OF_BOUNDS'
}


# Terrain speeds for my abilities
TERRAIN_SPEEDS = {
    'PAVED_ROAD': 4.5,
    'FOOTPATH': 3.5,
    'OPEN_LAND': 3.5,
    'EASY_MOVEMENT_FOREST': 3,
    'ROUGH_MEADOW': 2.5,
    'SLOW_RUN_FOREST': 2.5,
    'WALK_FOREST': 1.5,
    'IMPASSABLE_VEGETATION': 0,
    'LAKE_SWAMP_MARSH': 0,
    'OUT_OF_BOUNDS': 0
}


# # Terrain speeds planning for someone else
# TERRAIN_SPEEDS = {
#     'PAVED_ROAD': 3,
#     'FOOTPATH': 2,
#     'OPEN_LAND': 2,
#     'EASY_MOVEMENT_FOREST': 1.8,
#     'ROUGH_MEADOW': 1.4,
#     'SLOW_RUN_FOREST': 1.4,
#     'WALK_FOREST': 0.5,
#     'IMPASSABLE_VEGETATION': 0,
#     'LAKE_SWAMP_MARSH': 0,
#     'OUT_OF_BOUNDS': 0
# }


def draw_path_on_map(terrain_map, control, parents, course):
    """
    To plot a red colored path on the map
    :param terrain_map: Terrain map
    :param control: Current control
    :param parents: Dictionary of parents for each node
    :param course: To annotate the map based on the name of the course
    :return: None
    """
    pixel_map = terrain_map.load()
    while True:

        # To color the pixel with RED color as it is possibly the best color to depict the route:)
        pixel_map[control[0], control[1]] = PATH_COLOR

        # While the point has a parent we iteratively keep finding parents of the current node
        if parents[control] is not None:
            control = parents[control]
        else:
            break
    terrain_map.save("map_" + course + ".png")


def brute_force_permutations(adjacency_list, controls, time_limit, start_finish_coordinates):
    """
    To perform a modified depth first search
    :param adjacency_list: The adjacency list representation of the problem
    :param controls: The set of coordinates for the controls
    :param time_limit: The time limit specified on the file
    :param start_finish_coordinates: The start and finish coordinates
    :return: The successful permutation, the cost associated with that permutation and the number of controls visited
    """
    number_of_controls = len(controls)

    # Instead of infinite loop with break condition, using number_of_controls seemed more organic
    while number_of_controls >= 0:

        best_route = None

        # To get all the permutations of the controls
        control_permutations = permutations(controls, number_of_controls)

        for permutation in control_permutations:

            # To convert from an itertool object to a list
            permutation = list(permutation)

            # Not to forget the start and finish locations need to be the same hence we force insert them to the list
            permutation.insert(0, start_finish_coordinates)
            permutation.append(start_finish_coordinates)

            cost = 0
            number_of_controls_visited = 1
            for i in range(1, len(permutation)):

                # Looks far more complicated than what is happening :)
                # The adjacency list contains all control coordinates hence excluding the start coordinates we look for
                # the cost to the second set of controls in the first control list/dictionary and so on so forth
                # permutation[i-1] retrieves the adjacency list for the previous control
                # permutation[i] retrieves the entry for the current control in that list
                # [0] retrieves the cost in the list
                cost = cost + adjacency_list[permutation[i-1]][permutation[i]][0]
                number_of_controls_visited += 1

            if cost > time_limit:
                # If the time has exceeded the time limit no point looking further
                continue

            if number_of_controls_visited == len(permutation):
                if best_route and cost < best_route[0]:
                    best_route = (cost, permutation, number_of_controls_visited)
                else:
                    best_route = (cost, permutation, number_of_controls_visited)
        if best_route:
            return best_route
        number_of_controls = number_of_controls - 1


def is_goal(state, destination):
    """
    To check if the current state is the destination state
    :param state: The current node
    :param destination: Goal node
    :return: True/False
    """
    if state[0] == destination[0] and state[1] == destination[1]:
        return True
    return False


def successors(state):
    """
    To find a list of valid list_of_successors for the current state
    :param state: The current state whose neighbors we are attempting to find
    :return: List of list_of_successors
    """
    x, y = int(state[0]), int(state[1])

    list_of_successors = []

    # direction is helps determine the distance travelled while accounting for the cost, and hence the time
    # The if else cases are very verbose because I kept making mistakes with nesting the cases

    # An question one might have here is why not >= instead of > in the if else comparison, this is because
    # we check for the current pixel being less than 394 and 499, thus we can ensure that even the last pixel that
    # satisfies this condition (393, 498) has an adjoining pixel (394, 399) which can be added as a successor
    if x > MAP_START_X:
        list_of_successors.append((x - 1, y, 'Left'))
    if x < MAP_END_X:
        list_of_successors.append((x + 1, y, 'Right'))
    if y > MAP_START_Y:
        list_of_successors.append((x, y - 1, 'Top'))
    if y < MAP_END_Y:
        list_of_successors.append((x, y + 1, 'Bottom'))
    if x > MAP_START_X and y > MAP_START_Y:
        list_of_successors.append((x - 1, y - 1, 'Top_Left'))
    if x < MAP_END_X and y > MAP_START_Y:
        list_of_successors.append((x + 1, y - 1, 'Top_Right'))
    if x > MAP_START_X and y < MAP_END_Y:
        list_of_successors.append((x - 1, y + 1, 'Bottom_Left'))
    if x < MAP_END_X and y < MAP_END_Y:
        list_of_successors.append((x + 1, y + 1, 'Bottom_Right'))
    return list_of_successors


def cost_function(terrain_map, elevation_map, cost_to_node, current_pixel, next_pixel, destination):
    """
    To calculate the cost function
    :param terrain_map: The terrain map as a pixel object
    :param elevation_map: The elevation map
    :param cost_to_node: Cost from
    :param current_pixel: Current pixel coordinates
    :param next_pixel: Neighboring pixel coordinates
    :param destination: The destination coordinates
    :return: Cost of moving to the pixel
    """
    # Unpacking the next_pixel values
    direction = next_pixel[2]

    # This isn't really necessary but since we are using the integer values, I thought might as well unpack and
    # type cast to integer
    next_pixel = (int(next_pixel[0]), int(next_pixel[1]))

    # To get the current pixel and the next pixel terrains
    current_terrain = terrain_map[current_pixel[0], current_pixel[1]]
    next_terrain = terrain_map[next_pixel[0], next_pixel[1]]

    # Since the elevation matrix is a list of lists we go down through the rows and then across the columns
    current_elevation = elevation_map[current_pixel[1]][current_pixel[0]]
    next_elevation = elevation_map[current_pixel[1]][next_pixel[0]]

    # determine which direction we're going
    if direction == 'Top' or direction == 'Bottom':

        # moving up or down is depicted by the latitudinal distance
        distance = LATITUDE

    elif direction == 'Right' or direction == 'Left':

        # moving sideways is depicted by the longitudinal distance
        distance = LONGITUDE

    else:

        # moving along one of the diagonals
        distance = math.sqrt(LATITUDE ** 2 + LONGITUDE ** 2)

    # To find the difference in the elevation between the pixels
    elevation_difference = next_elevation - current_elevation

    # how steep is the gradient in terms of %
    gradient = (elevation_difference / distance) * 100

    current_terrain_speed = 0
    next_terrain_speed = 0

    if current_terrain in TERRAIN_PIXEL_VALUES:
        current_terrain_speed = TERRAIN_SPEEDS[TERRAIN_PIXEL_VALUES[current_terrain]]

    if next_terrain in TERRAIN_PIXEL_VALUES:
        next_terrain_speed = TERRAIN_SPEEDS[TERRAIN_PIXEL_VALUES[current_terrain]]

    # To perform all the time calculations

    # To check if we are in a swamp, marsh or lake
    if current_terrain_speed == 0 or next_terrain_speed == 0:
        time = math.inf

    else:
        # An attempt to get the ideal movement time by averaging the distance for the current and next pixel
        time_to_cross_current_pixel = float(distance/current_terrain_speed)
        time_to_cross_next_pixel = float(distance/next_terrain_speed)
        time = (1/2) * (time_to_cross_current_pixel + time_to_cross_next_pixel)

    # To account for time spent going up/down an incline/decline
    if gradient > 0:

        # If we are going uphill we gain 12-15s per mile as compared to moving on flat land
        #  and hence for 10m (latitude) we gain 0.0089s
        time += (distance * gradient * 0.0089)

    elif gradient < 0:

        # If we are going downhill we lose 8s per mile  as compared to moving on flat land and
        # hence for 10m (latitude) we lose about 0.0056s
        time -= (distance * gradient * 0.0056)
    else:
        pass

    cost_to_node[next_pixel] = cost_to_node[current_pixel] + time
    return cost_to_node[next_pixel] + get_heuristic_distance(next_pixel, destination)


def get_heuristic_distance(start, end):
    """
    To calculate the values for the heuristic function
    :param start: start coordinates in (x, y) values
    :param end: end coordinates in (x, y) values
    :return: diagonal distance between the 2 points
    """
    # Ideally heuristic function should be lesser than the actual distance between 2 points on the map,
    # and hence convenient to pick eucledian distance as the value for the heuristic function. However, if we can move
    # in a diagonal manner eucledian wouldn't perform as well as using diagonal distances
    start_x, start_y = start
    end_x, end_y = end

    D = LONGITUDE/4.5
    D_2 = math.sqrt(LATITUDE ** 2 + LONGITUDE ** 2)/4.5

    x_distance = abs(end_x - start_x)
    y_distance = abs(end_y - start_y)
    return D * (x_distance + y_distance) + (D_2 - 2 * D) * min(x_distance, y_distance)

# # Heuristic function for planning for someone else
# def get_heuristic_distance(start, end):
#     """
#     To calculate the values for the heuristic function
#     :param start: start coordinates in (x, y) values
#     :param end: end coordinates in (x, y) values
#     :return: eucledian distance between the 2 points
#     """
#     # Ideally heuristic function should be lesser than the actual distance between 2 points on the map, it becomes
#     # and hence convenient to pick eucledian distance as the value for the heuristic function
#     start_x, start_y = start
#     end_x, end_y = end
#
#     # To account for real-world pixel size
#     x_distance = abs(end_x - start_x) * LATITUDE
#     y_distance = abs(end_y - start_y) * LONGITUDE
#     return x_distance + y_distance
