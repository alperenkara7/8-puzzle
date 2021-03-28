initial_state = str([[5,4,0],[6,1,8],[7,3,2]])
final_state = str([[5,4,8],[6,0,1],[7,3,2]])

def expand(initial_state,final_state):
    """Successor function for the 8-puzzle variant
       Parameters
       ----------
       initial_state: 2-dimensional array representing initial 8-puzzle config
       Returns
       -------
       expanded_states: type- list of 2D arrrays
       """

    expanded_states = []
    print("---------------------------------\n"
          "---------------------------------")
    for i in bfs_for_expand(initial_state, final_state):
        expanded_states.append(i)
        print(i, end="\n")
    return expanded_states

def graph_search(initial_start,final_state):
    """Defines the path taken by the breadth-first search algorithm
       Parameters
       ----------
       initial_state: 2-dimensional array representing initial 8-puzzle config
       Returns
       -------
       path: (sequence of states to solve the 8-puzzle variant)type-list of 2D arrays
       """

    print("---------------------------------\n"
          "---------------------------------")
    path = []
    for i in bfs_graph(initial_state, final_state):
        print(">",i, end="\n")
        path.append(i)
    return path

def bfs_for_expand(initial_state, final_state):
    Visited_state = []
    state = [[initial_state]]
    while state:
        i = 0
        path = state[i]
        state = state[:i] + state[i + 1:]
        final = path[-1]
        if final in Visited_state:
            continue
        for moves in move(final):
            if moves in Visited_state:
                continue
            state.append(path + [moves])
        Visited_state.append(final)
        if final[16] == str(0): break
    return path

def move(state):
    moves = []
    direction = eval(state)
    i = 0
    j = 0
    while 0 not in direction[i]: i += 1
    j = direction[i].index(0)

    if i > 0:  # up
        direction[i][j], direction[i - 1][j] = direction[i - 1][j], direction[i][j]
        moves.append(str(direction))
        direction[i][j], direction[i - 1][j] = direction[i - 1][j], direction[i][j]

    if j < 2:  # right
        direction[i][j], direction[i][j + 1] = direction[i][j + 1], direction[i][j]
        moves.append(str(direction))
        direction[i][j], direction[i][j + 1] = direction[i][j + 1], direction[i][j]

    if j > 0:  # left
        direction[i][j], direction[i][j - 1] = direction[i][j - 1], direction[i][j]
        moves.append(str(direction))
        direction[i][j], direction[i][j - 1] = direction[i][j - 1], direction[i][j]

    if i < 2:  # down
        direction[i][j], direction[i + 1][j] = direction[i + 1][j], direction[i][j]
        moves.append(str(direction))
        direction[i][j], direction[i + 1][j] = direction[i + 1][j], direction[i][j]

    return moves

def bfs_graph(initial_state, final_state):
    Visited_state = []
    state = [[initial_state]]
    while state:
        i = 0
        path = state[i]
        state = state[:i] + state[i + 1:]
        final = path[-1]
        if final in Visited_state:
            continue
        for moves in move(final):
            if moves in Visited_state:
                continue
            state.append(path + [moves])
        Visited_state.append(final)
        if final == final_state: break
    return path


expand(initial_state,final_state)
graph_search(initial_state,final_state)