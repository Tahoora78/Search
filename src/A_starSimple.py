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
                if self.table[j][i].heuristicCost >= 1000000:
                    print("({},{}):".format(i, j), 'f', self.table[j][i].role, end = " ")
                else:
                    print("({},{}):".format(i, j), self.table[j][i].heuristicCost, self.table[j][i].role, end = " ")
            print()

    """
    find and set initial state
    """
    def initR(self):
        for j in range(self.row):
            for i in range(self.col):
                if (self.table[j][i].role == 'r'):
                    x = i
                    y = j
        print("x", x, "y", y, "->", self.table[y][x].cost, self.table[y][x].role)
        self.r = self.table[y][x]

    """
    update robot state
    """
    def setR(self, R):
        self.r = self.table[R.y][R.x]

    """
    find and set butter state(s)
    """
    def initB(self):
        for j in range(self.row):
            for i in range(self.col):
                if (self.table[j][i].role == 'b'):
                    self.b.append(self.table[j][i])

        for i in range(len(self.b)):
            print("x", self.b[i].x, "y", self.b[i].y, "->", self.b[i].cost, self.b[i].role)

    """
    update butter state
    """
    def setB(self, lastB, newB):
        self.b.remove(lastB)
        self.b.append(newB)

    """
    remove B and P
    """
    def removeB_P(self, B, P):
        self.b.remove(B)
        self.p.remove(P)

    """
    find and set goal state(s)
    """
    def initP(self):
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
    choose the best butter based on calculated heuristics
    """
    def chooseButter(self):
        minCost = 2000000
        for b in self.b:
            if (b.heuristicCost < minCost):
                minCost = b.heuristicCost
                if (minCost < 1000000):
                    print("selected butter:", b.x, b.y, b.role)
                    return b

        print("can’t pass the butter")
        return None

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
        Table.initR(self)
        Table.initB(self)
        Table.initP(self)

    """
    A_star search algorithm
    """
    def A_starSearch(self):
        # calculate the cost of each square from goalSquare
        for goal in self.p:
            Table.calculateCostsForSquares(self, goal, goal.x, goal.y)

            # print the table to check
            Table.printTable(self)

            # choose the butter to move
            b = Table.chooseButter(self)
            if (b == None): # can’t pass the butter
                return

            # start the algorithm
            graph = Graph(Node(self, self.r.x, self.r.y, b, 0), goal)
            result, update = graph.A_star(graph.node)
            self = update

            if result:
                print("Target is reachable from source")
            else:
                print("Target is NOT reachable from source")

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

class Node:
    def __init__(self, state, x, y, b, pathCost):
        self.state = state
        self.r_x = int(x)
        self.r_y = int(y)
        self.action = []
        self.heuristic = 0
        self.pathCost = pathCost
        self.totalCost = 0
        self.b = b
        Node.calculateHeuristic(self, pathCost)

    def calculateHeuristic(self, addPathCost):
        deltaX = abs(self.b.x - self.r_x)
        deltaY = abs(self.b.y - self.r_y)
        bSquareCost = self.b.heuristicCost
        self.pathCost += addPathCost
        print("deltaX", deltaX, "deltaY", deltaY, "bSquareCost", bSquareCost, "pathCost", self.pathCost)
        self.heuristic = bSquareCost + deltaX + deltaY
        self.totalCost = bSquareCost + self.pathCost + deltaX + deltaY

class Graph:
    def __init__(self, node, p):
        self.node = node
        self.graph = defaultdict(list)
        self.p = p

        self.fringeList = []
        self.fringeList.append(node)

        print("self.fringeList")
        for i in self.fringeList:
            print(i.r_x, i.r_y)

    """
    right action in table
    """
    def right(self, node):
        x = node.r_x
        y = node.r_y
        result = False
        isFinal = False
        if (x + 1) < node.state.col:
            if node.state.table[y][x+1].role != 'x':
                if node.state.table[y][x+1].role == 'b' and (x + 2) < node.state.col:
                    if node.state.table[y][x+2].role == 'n':
                        node.state.table[y][x+1].role = 'r'
                        node.state.table[y][x+2].role = 'b'
                        node.state.table[y][x].role = 'n'
                        node.state.setR(node.state.table[y][x+1])
                        node.state.setB(node.state.table[y][x+1], node.state.table[y][x+2])
                        node.b = node.state.table[y][x+2]
                        result = True

                    if node.state.table[y][x+2].role == 'p':
                        node.state.table[y][x+1].role = 'r'
                        node.state.table[y][x].role = 'n'
                        node.state.table[y][x+2].role = 'x'
                        node.state.setR(node.state.table[y][x+1])
                        node.state.removeB_P(node.state.table[y][x+1], node.state.table[y][x+2])
                        result = True
                        isFinal = True

                if (node.state.table[y][x+1].role != 'b') and (node.state.table[y][x+1].role != 'p'):
                    node.state.table[y][x].role = 'n'
                    node.state.table[y][x+1].role = 'r'
                    node.state.setR(node.state.table[y][x+1])
                    result = True

        if result:
            node.r_x += 1
            node.action.append('R')
            node.calculateHeuristic(node.state.table[y][x+1].cost)

            #node.state.printTable()
            print(node.totalCost)
            print(node.action)

        return result, node, isFinal

    """
    left action in table
    """
    def left(self, node):
        x = node.r_x
        y = node.r_y
        result = False
        isFinal = False
        if (x - 1) >= 0:
            if node.state.table[y][x-1].role != 'x':
                if node.state.table[y][x-1].role == 'b' and (x - 2) >= 0:
                    if node.state.table[y][x-2].role == 'n':
                        node.state.table[y][x-1].role = 'r'
                        node.state.table[y][x-2].role = 'b'
                        node.state.table[y][x].role = 'n'
                        node.state.setR(node.state.table[y][x-1])
                        node.state.setB(node.state.table[y][x-1], node.state.table[y][x-2])
                        node.b = node.state.table[y][x-2]
                        result = True

                    if node.state.table[y][x-2].role == 'p':
                        node.state.table[y][x-1].role = 'r'
                        node.state.table[y][x].role = 'n'
                        node.state.table[y][x-2].role = 'x'
                        node.state.setR(node.state.table[y][x-1])
                        node.state.removeB_P(node.state.table[y][x-1], node.state.table[y][x-2])
                        result = True
                        isFinal = True

                if (node.state.table[y][x-1].role != 'b') and (node.state.table[y][x-1].role != 'p'):
                    node.state.table[y][x].role = 'n'
                    node.state.table[y][x-1].role = 'r'
                    node.state.setR(node.state.table[y][x-1])
                    result = True

        if result:
            node.r_x -= 1
            node.action.append('L')
            node.calculateHeuristic(node.state.table[y][x-1].cost)

            #node.state.printTable()
            print(node.totalCost)
            print(node.action)

        return result, node, isFinal

    """
    up action in table
    """
    def up(self, node):
        x = node.r_x
        y = node.r_y
        result = False
        isFinal = False
        if (y - 1) >= 0:
            if node.state.table[y-1][x].role != 'x':
                if node.state.table[y-1][x].role == 'b' and (y - 2) >= 0:
                    if node.state.table[y-2][x].role == 'n':
                        node.state.table[y-1][x].role = 'r'
                        node.state.table[y-2][x].role = 'b'
                        node.state.table[y][x].role = 'n'
                        node.state.setR(node.state.table[y-1][x])
                        node.state.setB(node.state.table[y-1][x], node.state.table[y-2][x])
                        node.b = node.state.table[y-2][x]
                        result = True

                    if node.state.table[y-2][x].role == 'p':
                        node.state.table[y-1][x].role = 'r'
                        node.state.table[y][x].role = 'n'
                        node.state.table[y-2][x].role = 'x'
                        node.state.setR(node.state.table[y-1][x])
                        node.state.removeB_P(node.state.table[y-1][x], node.state.table[y-2][x])
                        result = True
                        isFinal = True

                if (node.state.table[y-1][x].role != 'b') and (node.state.table[y-1][x].role != 'p'):
                    node.state.table[y][x].role = 'n'
                    node.state.table[y-1][x].role = 'r'
                    node.state.setR(node.state.table[y-1][x])
                    result = True

        if result:
            node.r_y -= 1
            node.action.append('U')
            node.calculateHeuristic(node.state.table[y-1][x].cost)

            #node.state.printTable()
            print(node.totalCost)
            print(node.action)

        return result, node, isFinal

    """
    down action in table
    """
    def down(self, node):
        x = node.r_x
        y = node.r_y
        result = False
        isFinal = False
        if (y + 1) < node.state.row:
            if node.state.table[y+1][x].role != 'x':
                if node.state.table[y+1][x].role == 'b' and (y + 2) < node.state.row:
                    if node.state.table[y+2][x].role == 'n':
                        node.state.table[y+1][x].role = 'r'
                        node.state.table[y+2][x].role = 'b'
                        node.state.table[y][x].role = 'n'
                        node.state.setR(node.state.table[y+1][x])
                        node.state.setB(node.state.table[y+1][x], node.state.table[y+2][x])
                        node.b = node.state.table[y+2][x]
                        result = True

                    if node.state.table[y+2][x].role == 'p':
                        node.state.table[y+1][x].role = 'r'
                        node.state.table[y][x].role = 'n'
                        node.state.table[y+2][x].role = 'x'
                        node.state.setR(node.state.table[y+1][x])
                        node.state.removeB_P(node.state.table[y+1][x], node.state.table[y+2][x])
                        result = True
                        isFinal = True

                if (node.state.table[y+1][x].role != 'b') and (node.state.table[y+1][x].role != 'p'):
                    node.state.table[y][x].role = 'n'
                    node.state.table[y+1][x].role = 'r'
                    node.state.setR(node.state.table[y+1][x])
                    result = True

        if result:
            node.r_y += 1
            node.action.append('D')
            node.calculateHeuristic(node.state.table[y+1][x].cost)

            #node.state.printTable()
            print(node.totalCost)
            print(node.action)

        return result, node, isFinal

    """

    """
    def updateFringeList(self, node):
        self.fringeList.remove(node)
        newNodes = []
        isFinal = False

        r_result, r_next_node, isFinal = self.right(copy.deepcopy(node))
        if r_result:
            self.fringeList.append(r_next_node)
            newNodes.append(r_next_node)

        l_result, l_next_node, isFinal = self.left(copy.deepcopy(node))
        if l_result:
            self.fringeList.append(l_next_node)
            newNodes.append(l_next_node)

        u_result, u_next_node, isFinal = self.up(copy.deepcopy(node))
        if u_result:
            self.fringeList.append(u_next_node)
            newNodes.append(u_next_node)

        d_result, d_next_node,isFinal = self.down(copy.deepcopy(node))
        if d_result:
            self.fringeList.append(d_next_node)
            newNodes.append(d_next_node)

        #print("self.fringeList")
        #for i in self.fringeList:
        #    print(i.r_x, i.r_y)

        return newNodes, isFinal

    """
    check if state is goal
    """
    def check_goal(self, node):
        if self.p.x == node.b.x and self.p.y == node.b.y:
        #if (len(node.state.p) == 0):
            print("p.x", self.p.x, "b.x", node.b.x)
            print("p.y", self.p.y, "b.y", node.b.y)
            return True
        else:
            return False

    def calculateMinFringeCost(self):
        minTotalFringeCosts = 1000000
        node = None

        for n in self.fringeList:
            if n.totalCost < minTotalFringeCosts:
                minTotalFringeCosts = n.totalCost
                node = n

        return minTotalFringeCosts, node

    def findMinNewNode(self, newNodes):
        minCostOfNewNodes = 1000000
        node = None

        for n in newNodes:
            if self.check_goal(n):
                print("goal has achieved")
                return None, None

            if n.totalCost < minCostOfNewNodes:
                minCostOfNewNodes = n.totalCost
                node = n

        return minCostOfNewNodes, node

    """

    """
    def A_star(self, src):
        # first check if initial state is goal == (Table.p = None)
        if self.check_goal(src):
            print("initial state is goal")
            return True, src.state

        newNodes, isFinal = self.updateFringeList(src)

        while not isFinal:
            minCostOfNewNodes, minNewNode = self.findMinNewNode(newNodes)
            minTotalFringeCosts, midNode = self.calculateMinFringeCost()
            print("minCostOfNewNodes", minCostOfNewNodes)
            print("minTotalFringeCosts", minTotalFringeCosts)

            if minNewNode == None:
                return True, minNewNode

            if minCostOfNewNodes <= minTotalFringeCosts:
                print("we will continue")
                target = minNewNode
                print("selelelelelelel", target.action)
                newNodes, isFinal = self.updateFringeList(target)
            else:
                print("we should check again")
                target = midNode
                print("selelelelelelel", target.action)
                newNodes, isFinal = self.updateFringeList(target)

            target.state.printTable()

        return True, target

y, x = input().split()
states = Table(int(y), int(x))
Table.setTable(states)
Table.A_starSearch(states)