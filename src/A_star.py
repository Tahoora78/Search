from collections import defaultdict
import copy
from Ids import Node

class Graph:
    def __init__(self, node):
        # initial node(state)
        self.node = node
        # default dictionary to store graph
        self.graph = defaultdict(list)

    def heuristic(self, table, cell):
        """
        compute the heuristic of cell
        estimated cost for cell = manhattan distance (robot, butter, costs)
                                + manhattan distance (butter, goal, costs)
        """



    def addEdge(self, u, v):
        """
        add an edge to graph
        """
        self.graph[u].append(v)

    def print_states(self, node):
        """
        get a node and print all states under that node
        """
        print(len(node.state), " ", len(node.state[1]))
        for i in node.state:
            for j in i:
                print(j, end=" ")
            print()