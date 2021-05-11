from collections import defaultdict
import copy

class Table:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.table = []
        self.r = None
        self.b = []
        self.p = []

    def printTable(self):
        for i in range(self.row):
            for j in range(self.col):
                print("x", j, "y", i, "mohtava: ", self.table[j][i].cost)

    def setTable(self):
        initial_states = []
        for i in range(self.row):
            row = input().split()
            initial_states.append(row)

        # 2D array of squares
        for i in range(self.row):
            col = []
            for j in range(self.col):
                if(initial_states[i][j][0] != 'x'):
                    newSquare = Square(j, i, int(initial_states[i][j][0]))
                else:
                    newSquare = Square(j, i, 1000000)
                col.append(newSquare)
            self.table.append(col)
        Table.printTable(self)

        x = 0
        y = 0
        for i in range(len(initial_states)):
            for j in range(len(initial_states[i])):
                if 'r' in initial_states[i][j]:
                    x = i
                    y = j
        print("x", x, "y", y, "initial_state", initial_states[x][y])
        #initial_node = Ids.Node(initial_states, x, y, 0, 'N', int(initial_states[x][y][0]))

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

x, y = input().split()
states = Table(int(x), int(y))
Table.setTable(states)