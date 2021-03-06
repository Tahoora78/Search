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
    choose the best butter based on calculated heuristics
    """
    def chooseButter(self):
        minCost = 2000000
        for b in self.b:
            print("butter:", b.x, b.y, b.role, b.heuristicCost)
            if (b.heuristicCost < minCost):
                minCost = b.heuristicCost
                if (minCost < 1000000):
                    print("selected butter:", b.x, b.y, b.role)
                    return b

        print("can???t pass the butter")
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
        Table.setR(self)
        Table.setB(self)
        Table.setP(self)

    def findRobotGoal(self, butter):
        # first find the next butter's steps
        nextSteps = []
        if (butter.y > 0): #UP
            nextSteps.append(self.table[butter.y - 1][butter.x])
        if (butter.x > 0): #LEFT
            nextSteps.append(self.table[butter.y][butter.x - 1])
        if (butter.y < self.row - 1): #DOWN
            nextSteps.append(self.table[butter.y + 1][butter.x])
        if (butter.x < self.col - 1): #RIGHT
            nextSteps.append(self.table[butter.y][butter.x + 1])

        # find the best step(s)
        bestSteps = []
        minCost = 1000000
        for b in nextSteps:
            if (b.heuristicCost < minCost):
                minCost = b.heuristicCost
        for b in nextSteps:
            if (b.heuristicCost == minCost):
                bestSteps.append(b)

        # now find the robot's goal position
        for b in bestSteps:
            x = butter.x - (b.x - butter.x)
            y = butter.y - (b.y - butter.y)
            if (self.table[y][x].role != 'x'):
                print ("robot's goal position:", x, y)
                return self.table[y][x]

    """
    A_star search algorithm
    """
    def search(self):
        # calculate the cost of each square from goalSquare
        for goal in self.p:
            Table.calculateCostsForSquares(self, goal, goal.x, goal.y)

            # print the table to check
            Table.printTable(self)

            # choose the butter to move
            b = Table.chooseButter(self)
            if (b == None): # can???t pass the butter
                return

            # find the next step of butter and so determine the square which robot has to go there
            robotGoal = Table.findRobotGoal(self, b)

            # start the algorithm
            graph = Graph(Node(self, self.r.x, self.r.y, 'N', self.r.heuristicCost, 0 , robotGoal))
            if graph.A_star(graph.node, b):
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

        # print to check
        # print("x, y:", self.x, self.y, self.arrayCost, self.heuristicCost)

class Node:
    def __init__(self, state, x, y, action, squareCost, pathCost, robotGoal):
        self.state = state
        self.r_x = int(x)
        self.r_y = int(y)
        self.action = action
        self.heuristic = 0
        self.totalCost = 0
        self.robotGoal = robotGoal
        Node.calculateHeuristic(self, robotGoal, squareCost, pathCost)

    def calculateHeuristic(self, robotGoal, squareCost, pathCost):
        deltaX = abs(robotGoal.x - self.r_x)
        deltaY = abs(robotGoal.y - self.r_y)
        self.heuristic = squareCost + deltaX + deltaY
        self.totalCost = squareCost + pathCost + deltaX + deltaY

class Graph:
    def __init__(self, node):
        self.node = node
        self.graph = defaultdict(list)

        self.fringeList = []
        self.fringeList.append(node)

        print("self.fringeList")
        for i in self.fringeList:
            print(i.r_x, i.r_y)

    """

    """
    def updateFringeList(self, node):
        self.fringeList.remove(node)
        newNodes = []

        r_result, r_next_node = self.right(copy.deepcopy(node))
        if r_result:
            self.fringeList.append(r_next_node)
            newNodes.append(r_next_node)
            self.addEdge(node, r_next_node, 'R')

        l_result, l_next_node = self.left(copy.deepcopy(node))
        if l_result:
            self.fringeList.append(l_next_node)
            newNodes.append(l_next_node)
            self.addEdge(node, l_next_node, 'L')

        u_result, u_next_node = self.up(copy.deepcopy(node))
        if u_result:
            self.fringeList.append(u_next_node)
            newNodes.append(u_next_node)
            self.addEdge(node, u_next_node, 'U')

        d_result, d_next_node = self.down(copy.deepcopy(node))
        if d_result:
            self.fringeList.append(d_next_node)
            newNodes.append(d_next_node)
            self.addEdge(node, d_next_node, 'D')

        print("self.fringeList")
        for i in self.fringeList:
            print(i.r_x, i.r_y)

        return newNodes

    """

    """
    def goToButterPosition():


    """
    check if robot is at robotGoal
    """
    def check_robotGoal(self, node, robotGoal):
        if (node.state.r.x == robotGoal.x and node.state.r.y == robotGoal.y):
            return True
        else:
            return False

    """
    check if state is goal
    """
    def check_goal(self, node):
        if (len(node.state.p) == 0):
            return True
        else:
            return False

    """

    """
    def A_starForRobotGoal(self, src, b):
        goal = src.robotGoal
        result = False

        # check if robot reach the robotGoal position
        if self.check_robotGoal(src, goal):
            result = True
            target = src

            # so robot has tp go to the butter's position
            self.goToButterPosition()

        else:
            newNodes = self.updateFringeList(src)

        return result, target

    """

    """
    def A_star(self, src, b):
        # first check if initial state is goal == (Table.p = None)
        if self.check_goal(src):
            print("initial state is goal")
            return

        while (len(node.state.p) != 0):
            result, newButterPos = self.A_starForRobotGoal(src, b)
            if (result):


#######################################################################################################
    def addEdge(self, u, v, action):
        v.action = action
        self.graph[u].append(v)

    def up(self, node):
        x = node.r_x
        y = node.r_y
        result = False
        if (y - 1) >= 0:
            if 'x' not in node.state[y-1][x]:
                if 'b' in node.state[y-1][x] and (y - 2) >= 0:
                    if not('x' in node.state[y-2][x]) and not('p' in node.state[y-2][x]) and not('b' in node.state[y-2][x]):
                        node.state[y-1][x] = node.state[y-1][x].replace('b', 'r')
                        node.state[y-2][x] = node.state[y-2][x]+'b'
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        result = True
                        node.r_y -= 1
                        return result, node
                    if 'p' in node.state[y-2][x]:
                        node.state[y-1][x] = node.state[y-1][x].replace('b', 'r')
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        node.state[y-2][x] = node.state[y-2][x].replace('p', 'x')
                        result = True
                        node.r_y -= 1
                        return result, node
                if not('b' in node.state[y-1][x]) and not('p' in node.state[y-1][x]):
                    node.state[y][x] = node.state[y][x].replace('r', '')
                    node.state[y-1][x] = node.state[y-1][x]+'r'
                    result = True
                    node.r_y -= 1
                    return result, node
        return result, node

    def down(self, node):
        x = node.r_x
        y = node.r_y
        result = False
        if (y + 1) < len(node.state):
            if 'x' not in node.state[y+1][x]:
                if 'b' in node.state[y+1][x] and (y + 2) < len(node.state):
                    if not('x' in node.state[y+2][x]) and not('p' in node.state[y+2][x]) and not('b' in node.state[y+2][x]):
                        node.state[y+1][x] = node.state[y+1][x].replace('b', 'r')
                        node.state[y+2][x] = node.state[y+2][x]+'b'
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        result = True
                        node.r_y += 1
                        return result, node
                    if 'p' in node.state[y+2][x]:
                        node.state[y+1][x] = node.state[y+1][x].replace('b', 'r')
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        node.state[y+2][x] = node.state[y+2][x].replace('p', 'x')
                        result = True
                        node.r_y += 1
                        return result, node
                if not('b' in node.state[y+1][x]) and not('p' in node.state[y+1][x]):
                    node.state[y][x] = node.state[y][x].replace('r', '')
                    node.state[y+1][x] = node.state[y+1][x]+'r'
                    result = True
                    node.r_y += 1
                    return result, node
        return result, node

    def right(self, node):
        x = node.r_x
        y = node.r_y
        result = False
        if (x + 1) < len(node.state.col):
            if (node.state.table[y][x+1].role != 'x'):
                if node.state.table[y][x+1].role == 'b' and (x + 2) < len(node.state.col):
                    if not('x' in node.state[y][x+2]) and not('p' in node.state[y][x+2]) and not('b' in node.state[y][x+2]):
                        node.state[y][x+1] = node.state[y][x+1].replace('b', 'r')
                        node.state[y][x+2] = node.state[y][x+2]+'b'
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        result = True
                        node.r_x += 1
                        return result, node
                    if 'p' in node.state[y][x+2]:
                        node.state[y][x + 1] = node.state[y][x + 1].replace('b', 'r')
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        node.state[y][x + 2] = node.state[y][x + 2].replace('p','x')
                        result = True
                        node.r_x += 1
                        return result, node
                if not('b' in node.state[y][x+1]) and not('p' in node.state[y][x+1]):
                    node.state[y][x] = node.state[y][x].replace('r', '')
                    node.state[y][x+1] = node.state[y][x+1]+'r'
                    result = True
                    node.r_x += 1
                    return result, node
        return result, node

    def left(self, node):
        x = node.r_x
        y = node.r_y
        result = False
        if (x - 1) >= 0:
            if 'x' not in node.state[y][x-1]:
                if 'b' in node.state[y][x-1] and (x - 2) >= 0:
                    if not('x' in node.state[y][x-2]) and not('p' in node.state[y][x-2]) and not('b' in node.state[y][x-2]):
                        node.state[y][x-1] = node.state[y][x-1].replace('b', 'r')
                        node.state[y][x-2] = node.state[y][x-2]+'b'
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        result = True
                        node.r_x -= 1
                        return result, node
                    if 'p' in node.state[y][x-2]:
                        node.state[y][x - 1] = node.state[y][x - 1].replace('b', 'r')
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        node.state[y][x - 2] = node.state[y][x - 2].replace('p', 'x')
                        result = True
                        node.r_x -= 1
                        return result, node
                if not('b' in node.state[y][x-1]) and not('p' in node.state[y][x-1]):
                    node.state[y][x] = node.state[y][x].replace('r', '')
                    node.state[y][x-1] = node.state[y][x-1]+'r'
                    result = True
                    node.r_x -= 1
                    return result, node
        return result, node

    def print_state(self, node):
        print(len(node.state), " ", len(node.state[1]))
        for i in node.state:
            for j in i:
                print(j, end="  ")
            print()

    def find_key_value(self, val):
        for key, value in self.graph.items():
            if val in value:
                return key

y, x = input().split()
states = Table(int(y), int(x))
Table.setTable(states)
Table.search(states)