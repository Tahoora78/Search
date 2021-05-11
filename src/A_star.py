from collections import defaultdict
import copy

class Table:
    def __init__(self, row, col):
        self.col = col
        self.row = row
        self.table = []
        self.r = None
        self.b = []
        self.p = []

    """
    just for checking :D
    """
    def printTable(self):
        print("row", self.row, "col", self.col)
        for j in range(self.row):
            for i in range(self.col):
                print("({},{}):".format(i, j), self.table[j][i].cost, end = " ")
            print()

    def setR(self, initial_states):
        x = 0
        y = 0
        for j in range(self.row):
            for i in range(self.col):
                if 'r' in initial_states[j][i]:
                    x = i
                    y = j
                    print("i, j", i, j)
        print("x", x, "y", y, "initial_state", initial_states[y][x])
        #initial_node = Ids.Node(initial_states, x, y, 0, 'N', int(initial_states[x][y][0]))

    """
    Create the table with input values
    """
    def setTable(self):
        initial_states = []
        for i in range(self.row):
            row = input().split()
            initial_states.append(row)

        # 2D array of squares
        for j in range(self.row):
            col = []
            for i in range(self.col):
                # make each square
                if 'x' not in initial_states[j][i]:
                    newSquare = Square(i, j, int(initial_states[j][i][0]))
                else:
                    newSquare = Square(i, j, 1000000)

                col.append(newSquare)
            self.table.append(col)

        print(initial_states)

        # print the table to check
        Table.printTable(self)

        # find and set initial state
        Table.setR(self, initial_states)

        # now is time to calculate the cost of each square from goalSquare


class Square:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost
        self.heuristicCost = 0
        self.arrayCost = []

class Node:
    def __init__(self, state, x, y, action, cost):
        self.state = state
        self.r_x = int(x)
        self.r_y = int(y)
        self.action = action
        self.cost = cost

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

y, x = input().split()
states = Table(int(y), int(x))
Table.setTable(states)