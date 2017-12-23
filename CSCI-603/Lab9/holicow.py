__author__ = 'Rohit Ravishankar'
__author__ = 'Parinitha Nagaraja'

"""
CSCI-603: Lab 1
Author: Rohit Ravishankar (rr9105@rit.edu)
Author: Parinitha Nagaraja (pn4972@rit.edu)

This program implements graphs
"""

import sys
import math

from vertex import Vertex
from graph import Graph

COW = 'cow'
PAINTBALL = 'paintball'

class Holicow:

    __slots__ = 'graph', 'allVertices', 'cowColors', 'numberOfPaintsOnCows'
    def __init__(self, filename):
        """
        Initialize the graph the variables and the graph
        :param filename: File from where the input must be read
        """
        # initialize structures
        self.allVertices = []
        self.cowColors = dict()
        self.numberOfPaintsOnCows = dict()
        self.graph = Graph()

        # Create all the vertices
        with open(filename) as f:
            for line in f:
                line = line.strip()
                fields = line.split()
                if int(fields[2]) > 0 or int(fields[3]) > 0:
                    if len(fields) == 4:
                        vertex = Vertex(COW, fields[1], fields[2], fields[3] )
                        self.allVertices.append(vertex)
                    elif len(fields) == 5:
                        vertex = Vertex(PAINTBALL, fields[1], fields[2], fields[3], fields[4] )
                        self.allVertices.append(vertex)

        # Adding all vertices and edges between them
        for vertex in self.allVertices:
            if vertex.type == PAINTBALL:
                for otherVertex in self.allVertices:
                    distance = math.sqrt(((vertex.xcor - otherVertex.xcor)**2) + ((vertex.ycor - otherVertex.ycor)**2))
                    if distance <= vertex.radius and vertex.name != otherVertex.name:
                        self.graph.addEdge(vertex, otherVertex)

    def displayGraph(self):
        """
        To display the graph as an adjacency list
        :return: None
        """
        for vertex in self.graph.vertList:
            print(str(vertex) + ' connectedTo: ' + str([str(name) for name in self.graph.vertList[vertex].connectedTo]))

    def __traverseGraph(self,vertex,visited):
        """
        Recursively traverse the graph for each paintball vertex
        :param vertex: The vertex which needs to be traversed
        :param visited: The set of visited nodes
        :return:  None
        """
        dictionary = self.graph.vertList[vertex].connectedTo
        count = 0
        for paintballOrCow in dictionary:
            if dictionary[paintballOrCow].name not in visited:
                if dictionary[paintballOrCow].type == COW:
                    count += 1
                    print('\t'+dictionary[paintballOrCow].name + ' is painted ' + vertex)
                else:
                    print('\t'+str(dictionary[paintballOrCow].name) + ' paint ball was triggered by ' + vertex + ' paint ball ')
                    visited.add(dictionary[paintballOrCow].name)
                    count += self.__traverseGraph(dictionary[paintballOrCow].name,visited)
        return count

    def startTraversal(self):
        """
        Start the traversal to figure which nodes can be traversed when a paintball is triggered
        :return: None
        """
        for vertex in self.graph.vertList:
            visited = set()
            visited.add(vertex)
            if self.graph.vertList[vertex].type == PAINTBALL:
                print('\nTriggering ' + vertex + ' paint ball...')
                count = self.__traverseGraph(vertex,visited)
                self.numberOfPaintsOnCows.setdefault(vertex, int)
                self.numberOfPaintsOnCows[vertex] = count

    def addToCowColorsDictionary(self,cow,color):
        """
        Mark which cows are painted by what colors
        :param cow: Name of the cow
        :param color: The colors that paints the cow
        :return: None
        """
        if cow in self.cowColors:
            if color not in self.cowColors[cow]:
                self.cowColors[cow].append(color)
        else:
            self.cowColors.setdefault(cow,[])
            self.cowColors[cow].append(color)

    def traverseForBestPaintBall(self,vertex,visited):
        """
        To start the traversal from the maximum color paint ball
        :param vertex: Vertex that can make connections to other vertices
        :param visited: set of visited nodes
        :return:
        """
        dictionary = self.graph.vertList[vertex].connectedTo
        for paintballOrCow in dictionary:
            if dictionary[paintballOrCow].name not in visited:
                if dictionary[paintballOrCow].type == COW:
                    self.addToCowColorsDictionary(dictionary[paintballOrCow].name, vertex)
                else:
                    visited.add(dictionary[paintballOrCow].name)
                    self.traverseForBestPaintBall(dictionary[paintballOrCow].name, visited)

    def cowColorPrinting(self):
        """
        To print which cows were painted by what color
        :return: None
        """
        paintball = max(self.numberOfPaintsOnCows, key=self.numberOfPaintsOnCows.get)
        visited = set()
        self.traverseForBestPaintBall(paintball,visited)
        for vertex in self.allVertices:
            if vertex.type == COW:
                if vertex.name not in self.cowColors:
                    self.cowColors.setdefault(vertex.name, [])

        if self.checkIfNoCowsArePainted():
            print("Triggering the " +str(paintball)+" paint ball is the best choice with " +str(self.numberOfPaintsOnCows[paintball]) + " total paint on the cows:")
            for x in self.cowColors:
                print( x +"'s colors:" , self.cowColors[x])
        else:
            print("\tNo cows were painted by any starting paintball!")

    def checkIfNoCowsArePainted(self):
        """
        To check if now cows were painted
        :return: None
        """
        i = 0
        for x in self.cowColors:
            if not self.cowColors[x]:
                i += 1
        if i == len(self.cowColors):
            return False
        return True

def main():
    """
    Main code to test the functionality of the program
    :return: None
    """
    if len(sys.argv) < 2:
        print("Usage: python3 holicow.py {filename}")
        exit()
    else:
        try:
            holicow = Holicow(sys.argv[1])
            print('\nField of Dreams...')
            print('-----------------------------------------------------')
            holicow.displayGraph()
            print('\nBeginning simulation...')
            holicow.startTraversal()
            print('\nResults:')
            holicow.cowColorPrinting()
        except FileNotFoundError:
            print("File not found: {filename}")

if __name__ == '__main__':
    main()
