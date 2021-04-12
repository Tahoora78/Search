import Ids

def main():
    x, y = input().split()
    x = int(x)
    y = int(y)
    initial_states = []
    for i in range(x):
        row = input().split()
        initial_states.append(row)
    """
    for i in initial_states:
        for j in i:
            print(j, end=" ")
        print()
    """
    x = 0
    y = 0
    for i in range(len(initial_states)):
        for j in range(len(initial_states[i])):
            if 'r' in initial_states[i][j]:
                x = i
                y = j
    print("x", x, "y", y, "initial_state", initial_states[x][y])
    initial_nodes = Ids.Node(initial_states, x, y, 0, 'N')

    IdsAlgo(initial_nodes)

def IdsAlgo(initial_nodes):
    graph = Ids.Graph(initial_nodes)
    graph.print_state(initial_nodes)

def AstarAlgo(initial_nodes):
    pass

main()
