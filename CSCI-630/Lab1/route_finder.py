__author__ = 'Rohit Ravishankar'
__email__ = "rr9105@rit.edu"

from queue import PriorityQueue
from route_finder_utils import *

CLASSIC_COURSE = ["WHITE", "BROWN", "RED"]
SCORE_O = ["SCORE-O"]


def classic_route(terrain_map, modified_elevation_matrix, classic_courses):
    """
    To find the route for a classic event
    :param terrain_map: Map of terrain
    :param modified_elevation_matrix: Elevation matrix
    :param classic_courses: List of red, white & brown courses containing the start state and list of controls
    :return: None
    """
    # Convert the terrain map to a pixel object to access each pixel
    pixel_map = terrain_map.load()
    for i in range(len(classic_courses)):

        #  To pull the start and control information from route
        start, controls = classic_courses[i]

        # To store the cost for the route
        total_cost = 0

        source = start

        # To store the resulting map
        result_map = terrain_map.copy()

        for control in controls:

            # We get the cost and parents for each pixel and modify the source to the next pixel once we move
            parents, cost = path_A_star_search(pixel_map, modified_elevation_matrix, source, control)
            draw_path_on_map(result_map, control, parents, CLASSIC_COURSE[i])
            total_cost += cost

            # To update the source as the new.txt starting position
            source = control
        print("\nThe route taken was the classic", CLASSIC_COURSE[i], "route and it took",
              round(total_cost), "seconds to complete the course")


def scoreo_route(terrain_map, modified_elevation_matrix, scoreo_course):
    """
    To find the optimal scoreo route
    :param terrain_map: The terrain map
    :param modified_elevation_matrix: Elevation matrix
    :param scoreo_course: scoreo course file information
    :return: None
    """
    # Convert the terrain map to a pixel object to access each pixel
    pixel_map = terrain_map.load()

    # Unpacking values from the route
    time_limit, start_finish_coordinates, controls = scoreo_course

    # Creating a copy of the controls which is used to create an adjacency list
    copy_controls = controls.copy()

    # Adding the starting coordinates to the controls since we had removed it during the read process and the node is
    # needed for creating the adjacency list.
    # .insert() helps us insert at the start position of the list just like on the file
    copy_controls.insert(0, start_finish_coordinates)

    # Creating an adjacency list
    adjacency_list = create_adjacency_list(copy_controls, pixel_map, modified_elevation_matrix)

    # Notice that we don't send the copy of the list of controls(which has the first and last location appended) but
    # we use controls so that we can force the first and last location to be the start/finish coordinates to be the
    # particular start finish function
    cost, successful_permutation, number_of_controls_visited = brute_force_permutations(adjacency_list, controls,
                                                                                        time_limit,
                                                                                        start_finish_coordinates)

    # Copy of the result map to plot the route
    result_map = terrain_map.copy()
    controls.insert(0, start_finish_coordinates)

    # To keep track of the controls visited and the order
    visited_controls_order = []

    # Since we always find the route for the second control from the starting control which is fixed
    for i in range(1, len(successful_permutation)):
        visited_controls_order.insert(0, controls.index(successful_permutation[i]))
        draw_path_on_map(result_map, successful_permutation[i],
                         adjacency_list[successful_permutation[i-1]][successful_permutation[i]][1], SCORE_O[0])

    print("\nThe route taken was the Score-O route and it took",
          round(cost), "seconds to complete the course and visited", number_of_controls_visited,
          "controls where the finish control is considered as an additional control")


def create_adjacency_list(controls, pixel_map, elevation_matrix):
    """
    To create an adjacency list for the paths from each of the controls to all the other controls
    :param controls: The list of controls
    :param pixel_map: Pixel object of the terrain map
    :param elevation_matrix: Elevation matrix
    :return: Adjacency list representation of the controls
    """
    adjacency_list = {}
    # We iterate over the entire list of controls and connect it to other controls
    for control in controls:

        dict_other_controls = {}
        for other_control in controls:

            # To prevent the connection from the control to itself
            if control[0] != other_control[0] or control[1] != other_control[1]:

                # To find the shortest path between the current control and the other control
                parents, cost = path_A_star_search(pixel_map, elevation_matrix, control, other_control)

                # To add the distance and route to the other control into a dictionary
                dict_other_controls[other_control] = (cost, parents)

        # We finally add the shortest path to other controls to the current control
        adjacency_list[control] = dict_other_controls
    return adjacency_list


def path_A_star_search(pixel_map, modified_elevation_matrix, source, destination):
    """
    To find the path between 2 controls
    :param pixel_map: Terrain map in pixels
    :param modified_elevation_matrix: Elevation matrix
    :param source: Starting control
    :param destination: End control
    :return: Cost to destination node and dictionary storing information about parents
    """
    # Cost to source is 0 since it is the starting node
    cost_to_node = {source: 0}

    # To store the parents for each given node
    parents = {source: None}

    # Defining the priority queue for the A * search
    priority_queue = PriorityQueue()

    # Inserting the source node & associated cost into the priority queue
    priority_queue.put((0, source))

    # We continue the search while all possible successors are not eliminated
    while not priority_queue.empty():

        state = priority_queue.get()[1]

        # If the destination node is reached => :)
        if is_goal(state, destination):
            return parents, cost_to_node[destination]

        for si in successors(state):

            # To check if the successor is visited or not
            if (si[0], si[1]) not in parents:

                # Represents the cost of the travel, i.e., f = g + h, total cost = cost + heuristic_cost
                # We have to add the cost and node value to the priority queue since we've defined it that way
                # si[2] has the cardinal direction of the pixel from the current pixel which helps decide the elevation
                cost = cost_function(pixel_map, modified_elevation_matrix, cost_to_node, state, si, destination)

                successor = (int(si[0]), int(si[1]))

                # Add the successor to the priority queue
                priority_queue.put((cost, successor))

                # To append the current successor state to the dictionary for parents
                parents[(si[0], si[1])] = (state[0], state[1])
