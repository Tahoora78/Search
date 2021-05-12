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
                print("({},{}):".format(i, j), self.table[j][i].heuristicCost, self.table[j][i].role, end = " ")
            print()

    """
    find and set initial state
    """
    def setR(self):
        for j in range(self.row):
            for i in range(self.col):
                if (self.table[j][i].role == 'r'):
                    x = i
                    y = j
        print("x", x, "y", y, "->", self.table[y][x].cost, self.table[y][x].role)
        self.r = self.table[y][x]

    """
    find and set butter state(s)
    """
    def setB(self):
        for j in range(self.row):
            for i in range(self.col):
                if (self.table[j][i].role == 'b'):
                    self.b.append(self.table[j][i])

        for i in range(len(self.b)):
            print("x", self.b[i].x, "y", self.b[i].y, "->", self.b[i].cost, self.b[i].role)

    """
    find and set goal state(s)
    """
    def setP(self):
        for j in range(self.row):
            for i in range(self.col):
                if (self.table[j][i].role == 'p'):
                    self.p.append(self.table[j][i])

        for i in range(len(self.p)):
            print("x", self.p[i].x, "y", self.p[i].y, "->", self.p[i].cost, self.p[i].role)

    """
    set cost for all squares that are upper than the goalSquare
    """
    def calculateUP(self, x_g, y_g, term):
        if (y_g > 0):
            if (term == 1):
                for minusY in range(y_g - 1, -1, -1): # check y = (y_g-1 downto 0)
                    if (minusY > 0):
                        if (self.table[minusY - 1][x_g].cost != 1000000): # if the upper square is not x
                            # cost = cost of this Square + heuristicCost of the bottom square
                            cellCost = self.table[minusY][x_g].cost + self.table[minusY + 1][x_g].heuristicCost
                            self.table[minusY][x_g].addArrayCost(cellCost)
                        else:
                            self.table[minusY][x_g].addArrayCost(1000000)
                    else:
                        self.table[minusY][x_g].addArrayCost(1000000)

            if (term == 2):
                for minusY in range(y_g - 1, -1, -1): # check y = (y_g-1 downto 0)
                    if (minusY > 0):
                        if (x_g < self.col - 1): # if the square has right neighbour
                            if (self.table[minusY][x_g + 1].cost != 1000000): # if the right square is not x
                                cellCost = self.table[minusY][x_g].cost + self.table[minusY][x_g + 1].heuristicCost
                                self.table[minusY][x_g].addArrayCost(cellCost)
                            else:
                                self.table[minusY][x_g].addArrayCost(1000000)

                        if (x_g > 0): # if the square has left neighbour
                            if (self.table[minusY][x_g - 1].cost != 1000000): # if the left square is not x
                                cellCost = self.table[minusY][x_g].cost + self.table[minusY][x_g - 1].heuristicCost
                                self.table[minusY][x_g].addArrayCost(cellCost)
                            else:
                                self.table[minusY][x_g].addArrayCost(1000000)
    """
    set cost for all squares that are under the goalSquare
    """
    def calculateDOWN(self, x_g, y_g, term):
        if (y_g < self.row - 1):
            if (term == 1):
                for plusY in range(y_g + 1, self.row): # check y = (y_g+1 to row-1)
                    if (plusY < self.row - 1):
                        if (self.table[plusY + 1][x_g].cost != 1000000): # if the below square is not x
                            # cost = cost of this Square + heuristicCost of the top square
                            cellCost = self.table[plusY][x_g].cost + self.table[plusY - 1][x_g].heuristicCost
                            self.table[plusY][x_g].addArrayCost(cellCost)
                        else:
                            self.table[plusY][x_g].addArrayCost(1000000)
                    else:
                        self.table[plusY][x_g].addArrayCost(1000000)

            if (term == 2):
                for plusY in range(y_g + 1, self.row): # check y = (y_g+1 to row-1)
                    if (plusY < self.row - 1):
                        if (x_g < self.col - 1): # if the square has right neighbour
                            if (self.table[plusY][x_g + 1].cost != 1000000): # if the right square is not x
                                cellCost = self.table[plusY][x_g].cost + self.table[plusY][x_g + 1].heuristicCost
                                self.table[plusY][x_g].addArrayCost(cellCost)
                            else:
                                self.table[plusY][x_g].addArrayCost(1000000)

                        if (x_g > 0): # if the square has left neighbour
                            if (self.table[plusY][x_g - 1].cost != 1000000): # if the left square is not x
                                cellCost = self.table[plusY][x_g].cost + self.table[plusY][x_g - 1].heuristicCost
                                self.table[plusY][x_g].addArrayCost(cellCost)
                            else:
                                self.table[plusY][x_g].addArrayCost(1000000)

    """
    set cost for all squares that are at the left of the goalSquare
    """
    def calculateLEFT(self, x_g, y_g, term):
        if (x_g > 0):
            if (term == 1):
                for minusX in range(x_g - 1, -1, -1): # check x = (x_g-1 downto 0)
                    if (minusX > 0):
                        if (self.table[y_g][minusX - 1].cost != 1000000): # if the left square is not x
                            # cost = cost of this Square + heuristicCost of the right square
                            cellCost = self.table[y_g][minusX].cost + self.table[y_g][minusX + 1].heuristicCost
                            self.table[y_g][minusX].addArrayCost(cellCost)
                        else:
                            self.table[y_g][minusX].addArrayCost(1000000)
                    else:
                        self.table[y_g][minusX].addArrayCost(1000000)

            if (term == 2):
                for minusX in range(x_g - 1, -1, -1): # check x = (x_g-1 downto 0)
                    if (minusX > 0):
                        if (y_g < self.row - 1): # if the square has down neighbour
                            if (self.table[y_g + 1][minusX].cost != 1000000): # if the down square is not x
                                cellCost = self.table[y_g][minusX].cost + self.table[y_g + 1][minusX].heuristicCost
                                self.table[y_g][minusX].addArrayCost(cellCost)
                            else:
                                self.table[y_g][minusX].addArrayCost(1000000)

                        if (y_g > 0): # if the square has up neighbour
                            if (self.table[y_g - 1][minusX].cost != 1000000): # if the up square is not x
                                cellCost = self.table[y_g][minusX].cost + self.table[y_g - 1][minusX].heuristicCost
                                self.table[y_g][minusX].addArrayCost(cellCost)
                            else:
                                self.table[y_g][minusX].addArrayCost(1000000)

    """
    set cost for all squares that are at the right of the goalSquare
    """
    def calculateRIGHT(self, x_g, y_g, term):
        if (x_g < self.col - 1):
            if (term == 1):
                for plusX in range(x_g + 1, self.col): # check x = (x_g+1 to col-1)
                    if (plusX < self.col - 1):
                        if (self.table[y_g][plusX + 1].cost != 1000000): # if the right square is not x
                            # cost = cost of this Square + heuristicCost of the left square
                            cellCost = self.table[y_g][plusX].cost + self.table[y_g][plusX - 1].heuristicCost
                            self.table[y_g][plusX].addArrayCost(cellCost)
                        else:
                            self.table[y_g][plusX].addArrayCost(1000000)
                    else:
                        self.table[y_g][plusX].addArrayCost(1000000)

            if (term == 2):
                for plusX in range(x_g + 1, self.col): # check x = (x_g+1 to col-1)
                    if (plusX < self.col - 1):
                        if (y_g < self.row - 1): # if the square has down neighbour
                            if (self.table[y_g + 1][plusX].cost != 1000000): # if the down square is not x
                                cellCost = self.table[y_g][plusX].cost + self.table[y_g + 1][plusX].heuristicCost
                                self.table[y_g][plusX].addArrayCost(cellCost)
                            else:
                                self.table[y_g][plusX].addArrayCost(1000000)

                        if (y_g > 0): # if the square has up neighbour
                            if (self.table[y_g - 1][plusX].cost != 1000000): # if the up square is not x
                                cellCost = self.table[y_g][plusX].cost + self.table[y_g - 1][plusX].heuristicCost
                                self.table[y_g][plusX].addArrayCost(cellCost)
                            else:
                                self.table[y_g][plusX].addArrayCost(1000000)

    """
    Calculate a heuristic cost for each square based on distance and squares' costs.
    """
    def calculateCostsForSquares(self, goalSquare, x_g, y_g):
        # set the cost of goalSquare to zero
        self.table[y_g][x_g].addArrayCost(0)
        self.table[y_g][x_g].heuristicCost = 0

        # up, down, left, right
        Table.calculateUP(self, x_g, y_g, 1)
        Table.calculateDOWN(self, x_g, y_g, 1)
        Table.calculateLEFT(self, x_g, y_g, 1)
        Table.calculateRIGHT(self, x_g, y_g, 1)

        # up and left
        if (y_g > 0) and (x_g > 0):
            for minusX in range(x_g - 1, -1, -1): # check x = (x_g-1 downto 0)
                Table.calculateUP(self, minusX, y_g, 1)
            for minusY in range(y_g - 1, -1, -1): # check y = (y_g-1 downto 0)
                Table.calculateLEFT(self, x_g, minusY, 1)

        # down and left
        if (y_g < self.row - 1) and (x_g > 0):
            for minusX in range(x_g - 1, -1, -1): # check x = (x_g-1 downto 0)
                Table.calculateDOWN(self, minusX, y_g, 1)
            for plusY in range(y_g + 1, self.row): # check y = (y_g+1 to row-1)
                Table.calculateLEFT(self, x_g, plusY, 1)

        # up and right
        if (y_g > 0) and (x_g < self.col - 1):
            for plusX in range(x_g + 1, self.col): # check x = (x_g+1 to col-1)
                Table.calculateUP(self, plusX, y_g, 1)
            for minusY in range(y_g - 1, -1, -1): # check y = (y_g-1 downto 0)
                Table.calculateRIGHT(self, x_g, minusY, 1)

        # down and right
        if (y_g < self.row - 1) and (x_g < self.col - 1):
            for plusX in range(x_g + 1, self.col): # check x = (x_g+1 to col-1)
                Table.calculateDOWN(self, plusX, y_g, 1)
            for plusY in range(y_g + 1, self.row): # check y = (y_g+1 to row-1)
                Table.calculateRIGHT(self, x_g, plusY, 1)

        # up, down, left, right
        Table.calculateUP(self, x_g, y_g, 2)
        Table.calculateDOWN(self, x_g, y_g, 2)
        Table.calculateLEFT(self, x_g, y_g, 2)
        Table.calculateRIGHT(self, x_g, y_g, 2)

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
                    if 'r' in initial_states[j][i]:   # robot role
                        newSquare = Square(i, j, int(initial_states[j][i][0]), 'r')
                    elif 'b' in initial_states[j][i]: # butter role
                        newSquare = Square(i, j, int(initial_states[j][i][0]), 'b')
                    elif 'p' in initial_states[j][i]: # goal role
                        newSquare = Square(i, j, int(initial_states[j][i][0]), 'p')
                    else:                             # normal role
                        newSquare = Square(i, j, int(initial_states[j][i][0]), 'n')
                else:                                 # x role
                    newSquare = Square(i, j, 1000000, 'x')

                col.append(newSquare)
            self.table.append(col)

        # find and set initial state, butter state(s) and goal state(s)
        Table.setR(self)
        Table.setB(self)
        Table.setP(self)

        # now is time to calculate the cost of each square from goalSquare
        for goal in self.p:
            Table.calculateCostsForSquares(self, goal, goal.x, goal.y)

            # print the table to check
            Table.printTable(self)

class Square:
    def __init__(self, x, y, cost, role):
        self.x = x
        self.y = y
        self.cost = cost
        self.role = role
        self.heuristicCost = 0
        self.arrayCost = []

    """
    Add the new cost and update heuristicCost
    """
    def addArrayCost(self, c):
        self.arrayCost.append(c)

        minH = min(self.arrayCost)
        self.heuristicCost = minH

        # print to check
        # print("x, y:", self.x, self.y, self.arrayCost, self.heuristicCost)

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


y, x = input().split()
states = Table(int(y), int(x))
Table.setTable(states)