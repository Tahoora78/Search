from collections import defaultdict
import copy

class Node:
    def __init__(self, state, x, y, action):
        """
        :param state:
        :param x: x position of robot
        :param y: y position of robot
        :param action:'D','U','R','L' ,'N'
        """
        self.state = state
        self.r_x = int(x)
        self.r_y = int(y)
        self.action = action


class Graph:
    def __init__(self, node):
        # initial node(state)
        self.node = node
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
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
        if (x + 1) < len(node.state[0]):
            if 'x' not in node.state[y][x+1]:
                if 'b' in node.state[y][x+1] and (x + 2) < len(node.state[0]):
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

    def producing_next_node(self, node):
        next_node = copy.deepcopy(node)
        result, next_node = self.right(next_node)
        if result:
            print("success")
            self.addEdge(node, next_node)


    def print_state(self, node):
        print(len(node.state), " ", len(node.state[1]))
        for i in node.state:
            for j in i:
                print(j, end="  ")
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

def main():
    x, y = input().split()
    x = int(x)
    y = int(y)
    initial_states = []
    for i in range(x):
        row = input().split()
        initial_states.append(row)
    x = 0
    y = 0
    for i in range(len(initial_states)):
        for j in range(len(initial_states[i])):
            if 'r' in initial_states[i][j]:
                y = i
                x = j
    print("x", x, "y", y, "initial_state", initial_states[x][y])
    graph = Graph(Node(initial_states, x, y, 'N'))
    graph.print_state(graph.node)
    result, node = graph.down(graph.node)
    graph.print_state(node)
main()