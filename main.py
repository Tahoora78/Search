import Ids
import A_star

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
                x = i
                y = j
    print("x", x, "y", y, "initial_state", initial_states[x][y])
    initial_node = Ids.Node(initial_states, x, y, 0, 'N', int(initial_states[x][y][0]))

    IdsAlgo(initial_node)

def IdsAlgo(initial_node):
    graph = Ids.Graph(initial_node)
    graph.print_state(initial_node)
    initial_node.getCost()

def AstarAlgo(initial_node):
    graph = A_star.Graph(initial_node)
    graph.print_state(initial_node)

main()
