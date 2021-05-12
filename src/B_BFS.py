from collections import defaultdict

class Node:
    def __init__(self, state, x, y, action):
        self.state = state
        self.r_x = int(x)
        self.r_y = int(y)
        self.action = action


class Graph:

    b_states = []

    def __init__(self, src_node, des_node, b_state):
        self.src_node = src_node
        self.des_node = des_node
        self.src_graph = defaultdict(list)
        self.des_graph = defaultdict(list)
        Graph.b_states = b_state

    def add_src_edge(self, u, v):
        self.src_graph[u].append(v)

    def add_des_edge(self, u, v):
        self.des_graph[u].append(v)

    @staticmethod
    def check_similar(node1, node2):
        for row in range(len(node1.state)):
            for j in range(len(node1.state[row])):
                if node1.state[row][j] != node2[row][j]:
                    return False
        return True

    @staticmethod
    def check_intersect(src_visited, des_visited):
        for i in src_visited:
            if i in des_visited:
                return True
        return False

    def find_key_value(self, val, dictionary):
        for key, value in dictionary.items():
            if val in value:
                return key

    def print_src_result(self, node):
        parent_list = []
        parent_list.append(node)
        parent = self.find_key_value(node, self
                                     .src_graph)
        while parent != self.src_node:
            parent_list.append(parent)
            node = parent
            parent = self.find_key_value(node, self.src_graph)
        parent_list.append(self.src_node)
        parent_list = parent_list[::-1]
        for i in parent_list:
            print(i, end=" ")

    def print_dst_result(self, node):
        parent_list = []
        parent_list.append(node)
        parent = self.find_key_value(node, self.des_graph)
        while parent != self.des_node:
            parent_list.append(parent)
            node = parent
            parent = self.find_key_value(node, self.des_graph)
        parent_list.append(self.des_node)
        for i in parent_list:
            print(i, end=" ")

    def up(self, node):
        x = node.r_x
        y = node.r_y
        result = False
        if (y - 1) >= 0:
            if 'x' not in node.state[y-1][x] and 's' not in node.state[y-1][x]:
                if 'b' in node.state[y-1][x] and (y - 2) >= 0:
                    if not('x' in node.state[y-2][x]) and not('x' in node.state[y-2][x])\
                            and not('p' in node.state[y-2][x]) and not('b' in node.state[y-2][x]):
                        node.state[y-1][x] = node.state[y-1][x].replace('b', 'r')
                        node.state[y-2][x] = node.state[y-2][x]+'b'
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        result = True
                        node.r_y -= 1
                        return result, node
                    if 'p' in node.state[y-2][x]:
                        node.state[y-1][x] = node.state[y-1][x].replace('b', 'r')
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        node.state[y-2][x] = node.state[y-2][x].replace('p', 's')
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
            if 'x' not in node.state[y+1][x] and 's' not in node.state[y+1][x]:
                if 'b' in node.state[y+1][x] and (y + 2) < len(node.state):
                    if not('x' in node.state[y+2][x]) and not('s' in node.state[y+2][x]) \
                            and not('p' in node.state[y+2][x]) and not('b' in node.state[y+2][x]):
                        node.state[y+1][x] = node.state[y+1][x].replace('b', 'r')
                        node.state[y+2][x] = node.state[y+2][x]+'b'
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        result = True
                        node.r_y += 1
                        return result, node
                    if 'p' in node.state[y+2][x]:
                        node.state[y+1][x] = node.state[y+1][x].replace('b', 'r')
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        node.state[y+2][x] = node.state[y+2][x].replace('p', 's')
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
            if 'x' not in node.state[y][x+1] and 's' not in node.state[y][x+1]:
                if 'b' in node.state[y][x+1] and (x + 2) < len(node.state[0]):
                    if not('x' in node.state[y][x+2]) and not('s' in node.state[y][x+2]) and\
                            not('p' in node.state[y][x+2]) and not('b' in node.state[y][x+2]):
                        node.state[y][x+1] = node.state[y][x+1].replace('b', 'r')
                        node.state[y][x+2] = node.state[y][x+2]+'b'
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        result = True
                        node.r_x += 1
                        return result, node
                    if 'p' in node.state[y][x+2]:
                        node.state[y][x + 1] = node.state[y][x + 1].replace('b', 'r')
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        node.state[y][x + 2] = node.state[y][x + 2].replace('p', 's')
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
            if 'x' not in node.state[y][x-1] and 's' not in node.state[y][x-1]:
                if 'b' in node.state[y][x-1] and (x - 2) >= 0:
                    if not('x' in node.state[y][x-2]) and not('s' in node.state[y][x-2])\
                            and not('p' in node.state[y][x-2]) and not('b' in node.state[y][x-2]):
                        node.state[y][x-1] = node.state[y][x-1].replace('b', 'r')
                        node.state[y][x-2] = node.state[y][x-2]+'b'
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        result = True
                        node.r_x -= 1
                        return result, node
                    if 'p' in node.state[y][x-2]:
                        node.state[y][x - 1] = node.state[y][x - 1].replace('b', 'r')
                        node.state[y][x] = node.state[y][x].replace('r', '')
                        node.state[y][x - 2] = node.state[y][x - 2].replace('p', 's')
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




    def up_d(self, node):
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
                        node.state[y-2][x] = node.state[y-2][x].replace('p', 's')
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

    def down_d(self, node):
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
                        node.state[y+2][x] = node.state[y+2][x].replace('p', 's')
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

    def right_d(self, node):
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
                        node.state[y][x + 2] = node.state[y][x + 2].replace('p', 's')
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

    def left_d(self, node):
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
                        node.state[y][x - 2] = node.state[y][x - 2].replace('p', 's')
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

    def finding_result_node(self):
        self.des_node = self.src_node.copy()
        x_p = -1
        y_p = -1
        for i in range(len(self.src_node.state)):
            for j in range(len(self.src_node.state[i])):
                if 'b' in self.src_node.state[i][j]:
                    self.des_node[i][j] = self.des_node[i][j].replace('b', '')
                if 'r' in self.src_node.state[i][j]:
                    self.des_node[i][j] = self.des_node[i][j].replace('r', '')
                if 'p' in self.src_node.state[i][j]:
                    self.des_node[i][j] = self.des_node[i][j].replace('p', 's')
                    if x_p ==-1 and y_p==-1:
                        x_p = j
                        y_p = i
                        #self.des_node.r_x = j
                        #self.des_node.r_y = i


    def BFS(self):
        src_queue = []
        des_queue = []
        src_visited = []
        des_visited = []

        src_queue.append(self.src_node)
        des_queue.append(self.des_node)

        src_visited.append(self.src_node)
        des_visited.append(self.des_node)

        src_result = []
        des_result = []

        while not self.check_intersect(src_visited, des_visited):
            ss = src_queue.pop(0)
            sd = des_queue.pop(0)
            src_result.append(ss)
            des_result.append(sd)
            #print(ss, end=" ")
            #print(sd, end=" ")

            for i in self.src_graph[ss]:
                if not(i in src_visited):
                    src_queue.append(i)
                    src_visited.append(i)


            for i in self.des_graph[sd]:
                if not(i in des_visited):
                    des_queue.append(i)
                    des_visited.append(i)
        des_result = des_result[::-1]
        self.print_src_result(src_result[-1])
        #print("desresult0 ", des_result)
        self.print_dst_result(des_result[0])
        return src_result+des_result

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
    b_states = []
    for i in range(len(initial_states)):
        for j in range(len(initial_states[i])):
            if 'r' in initial_states[i][j]:
                y = i
                x = j
            if 'b' in initial_states[i][j]:
                b_states.append([j, i])
    graph = Graph(Node(initial_states, x, y, 'N', b_states))
