class Node:
    def __init__(self, state, depth, cost):
        self.state = state
        self.depth = depth
        self.cost = cost


class Move:
    def __init__(self, node):
        self.node_graph = []
        self.node_graph.append(node)

    def next_state(self, node):
        #return the following node
        pass

    def check_goal(self, node):
        pass


def main():
    x, y = input().split()
    x = int(x)
    y = int(y)
    initial_state = []
    for i in range(x):
        row = input().split()
        initial_state.append(row)
    """
    for i in initial_state:
        for j in i:
            print(j, end=" ")
        print()
    """
    move = Move(Node(initial_state, 0, 0))

main()