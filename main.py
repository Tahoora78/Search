import Ids

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
    x = 0
    y = 0
    for i in range(len(initial_state)):
        for j in range(len(initial_state[i])):
            if 'r' in initial_state[i][j]:
                x = j
                y = i
    print("x", x, "y", y, "initial_state", initial_state[x][y])
    initial_node = Ids.Node(initial_state, x, y, 0, 'N')
    graph = Ids.Graph(initial_node)

    graph.print_state(initial_node)

main()
