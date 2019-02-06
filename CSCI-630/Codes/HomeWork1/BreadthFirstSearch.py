__author__ = "Rohit Ravishankar"
__email__ = "rr9105@rit.edu"

import math

STARTING_NODE = 4


def list_of_successors(number):
    """
    To create a list of successors of the current node
    :param number: The number whose successors must be created
    :return: List of successors
    """
    successors = []

    successors.append(int(math.sqrt(number)))
    successors.append(math.floor(number))
    if number <= 197:
        successors.append(math.factorial(number))

    return successors


def traverse(parents, path, goal):
    """
    To return the path from the goal to the parent
    :param parents: Dictionary containing information about nodes and their parents
    :param path: List to store the path
    :param goal: The goal node
    :return:  sequence of numbers required to reach the goal
    """
    if goal in parents:
        path.append(goal)
        traverse(parents, path, parents.get(goal))

    return path


def bfs(goal):
    """
    Construct the BFS to reach any goal integer when starting with the number 4 and performing a sequence of factorial,
    square root and floor operations will reach any desired positive integer.
    :param goal: goal integer to be achieved
    :return: Path to the goal
    """

    # Queue to store successors
    queue = []

    # Visited nodes
    visited = {}

    # To store information about parent nodes
    parents = {}

    # Queue to store the root node
    queue.append(STARTING_NODE)

    # Mark the starting node as visited
    visited[STARTING_NODE] = True

    while queue:

        state = queue.pop(0)
        if state == goal:
            break

        # Pull out the list of successors for the current node
        successors = list_of_successors(state)

        # Traverse each of the successor nodes
        for successor in successors:
            if successor not in visited:
                queue.append(successor)
                parents[successor] = state
                visited[successor] = True

    # If there are parents to the goal node
    if parents:
        traversal_list = traverse(parents, [], goal)
        traversal_list.append(STARTING_NODE)
        print(traversal_list)
    else:
        print(state)


if __name__ == "__main__":
    bfs(5)
    bfs(8)
    bfs(10)
    bfs(13)
