from collections import defaultdict
import copy


class Node:
    def __init__(self, state, x, y, action):
        self.state = state
        self.r_x = int(x)
        self.r_y = int(y)
        self.action = action


class Graph:
    def __init__(self, node):
        self.node = node
        self.graph = defaultdict(list)
        self.last_level_node = []
        self.last_level_node.append(node)

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

    def check_goal(self, node):
        result = True
        for i in node.state:
            for j in i:
                if 'p' in j:
                    result = False
                    return result
        return result

    def producing_one_level_node(self):
        level_node = []
        for node in self.last_level_node:
            level_node = self.producing_next_node(node, level_node)
        self.last_level_node = level_node
        #print("======================================================")
        #for i in self.last_level_node:
         #   print(':LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL')
          #  self.print_state(i)
           # print('LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL')
        #print("=================================-------------------------")

    def producing_next_node(self, node, level_node):
        next_node = copy.deepcopy(node)
        r_result, r_next_node = self.right(copy.deepcopy(node))
        if r_result:
            level_node.append(r_next_node)
            self.addEdge(node, r_next_node, 'R')
        l_result, l_next_node = self.left(copy.deepcopy(node))
        if l_result:
            level_node.append(l_next_node)
            self.addEdge(node, l_next_node, 'L')
        u_result, u_next_node = self.up(copy.deepcopy(node))
        if u_result:
            level_node.append(u_next_node)
            self.addEdge(node, u_next_node, 'U')
        d_result, d_next_node = self.down(copy.deepcopy(node))
        if d_result:
            level_node.append(d_next_node)
            self.addEdge(node, d_next_node, 'D')
        return level_node

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

    def DLS(self, src, maxDepth):
        if self.check_goal(src):
            return True, src
        if maxDepth <= 0:
            return False, None

        for i in self.graph[src]:
            result, target = self.DLS(i, maxDepth - 1)
            if result:
                return True, target
        return False, None

    def IDDFS(self, src, maxDepth):
        result = False
        #for i in range(maxDepth):
        i=0
        while result!=True:
            print("ii", i)
            if i != 0:
                self.producing_one_level_node()
            result, target = self.DLS(src, i)
            i +=1
        if result:
                i -= 1
                print("result", result)
                final_list = []
                #print("graph", self.graph)
                depth = i
                final_list.append(target)
                pre_node1 = self.find_key_value(target)
                final_list.append(pre_node1)
                for i in range(i - 1):
                    pre_node1 = self.find_key_value(pre_node1)
                    final_list.append(pre_node1)
                for i in range(len(final_list) - 2, -1, -1):
                    print(final_list[i].action, end=' ')
                for m in range(len(final_list) - 2, -1, -1):
                    print()
                    print("::::::::::::::::::::::::::::::::::::")
                    self.print_state(final_list[m])
                    print("::::::::::::::::::::::::::::::::::::::::::")
                    #print(final_list[m], end=' ')
                print()
                cost = len(final_list)-1
                print(cost)
                print(depth)
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
    graph = Graph(Node(initial_states, x, y, 'N'))
    if graph.IDDFS(graph.node, 6):
        print("Target is reachable from source " +
              "within max depth")
    else:
        print("Target is NOT reachable from source " +
              "within max depth")
main()