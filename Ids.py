from collections import defaultdict
import copy

class Node:
    def __init__(self, state, x, y, depth, action):
        self.state = state
        self.x = int(x)
        self.y = int(y)
        self.depth = depth
        self.action = action
        #self.cost = cost


class Graph:
    def __init__(self, node):
        # initial node(state)
        self.node = node
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)


    def right(self, node):
        x = node.x
        y = node.y
        if (x + 1) < len(node.state[0]):
            if 'x' not in node.state[x + 1][y]:
                if 'b' in node.state[x + 1][y] and (x + 2) < len(node.state[0]):
                    if 'x' in node.state[x + 2][y]:
                        return False, None
                    else:
                        node.state[x + 1][y] = node.state[x + 1][y].replace('b', 'r')
                        node.state[x+2][y] = node.state[x+2][y]+'b'
                        node.state[x][y] = node.state[x][y].replace('r', '')
                        return True, node.state
                else:
                    node.state[x][y] = node.state[x][y].replace('r', '')
                    node.state[x+1][y] = node.state[x+1][y]+'r'
                    return True, node.state
            else:
                return False,None
        else:
            return False, None

    def producing_next_node(self, node):
        next_node = copy.deepcopy(self.n)

        pass

    def print_state(self, node):
        print(len(node.state), " ", len(node.state[1]))
        for i in node.state:
            for j in i:
                print(j, end=" ")
            print()

    def DLS(self, src, target, maxDepth):

        if src == target: return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0: return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
            if (self.DLS(i, target, maxDepth - 1)):
                return True
        return False

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self, src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False
