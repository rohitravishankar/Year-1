"""
CSCI-603: Graphs
Author: Sean Strout @ RIT CS
Author: Rohit Ravishankar (rr9105@rit.edu)
Author: Parinitha Nagaraja (pn4972@rit.edu)

An implementation of a vertex as part of a graph.

Code taken from the online textbook and modified:

http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
"""

COW = 'cow'
PAINTBALL = 'paintball'

class Vertex:
    """
    An individual vertex in the graph.

    :slots: id:  The identifier for this vertex (user defined, typically
        a string)
    :slots: connectedTo:  A dictionary of adjacent neighbors, where the key is
        the neighbor (Vertex), and the value is the edge cost (int)
    """

    __slots__ = 'type', 'name', 'connectedTo', 'xcor', 'ycor', 'radius'

    def __init__(self, type, name, xcor, ycor, radius = 0 ):
        """
        Initialize a vertex
        :param key: The identifier for this vertex
        :return: None
        """
        self.type = type
        self.name = name
        self.xcor = int(xcor)
        self.ycor = int(ycor)
        self.radius = int(radius)
        self.connectedTo = {}

    def addNeighbor(self, nbr):
        """
        Connect this vertex to a neighbor with a given weight (default is 0).
        :param nbr (Vertex): The neighbor vertex
        :param weight (int): The edge cost
        :return: None
        """
        self.connectedTo[nbr.name] = nbr

    def __str__(self):
        """
        Return a string representation of the vertex and its direct neighbors:

            vertex-id connectedTo [neighbor-1-id, neighbor-2-id, ...]

        :return: The string
        """
        return str(self.id) + ' connectedTo: ' + str([str(x.id) for x in self.connectedTo])

    def getConnections(self):
        """
        Get the neighbor vertices.
        :return: A list of Vertex neighbors
        """
        return self.connectedTo.keys()

    def getWeight(self, nbr):
        """
        Get the edge cost to a neighbor.
        :param nbr (Vertex): The neighbor vertex
        :return: The weight (int)
        """
        return self.connectedTo[nbr]