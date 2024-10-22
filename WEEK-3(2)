import heapq

def manhattan_distance(state, goal):
    """Calculate the Manhattan distance."""
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_index = goal.index(state[i])
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_index, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

class Node:
    def __init__(self, state, parent=None, depth=0, cost=0, h=0):
        self.state = state
        self.parent = parent
        self.depth = depth 
        self.cost = cost  
        self.h = h  

    def __lt__(self, other):
        return self.cost < other.cost

def astar_manhattan(initial_state, goal_state):
    def get_neighbors(state):
        neighbors = []
        zero_idx = state.index(0)
        x, y = divmod(zero_idx, 3)
        moves = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
        for move, (dx, dy) in moves.items():
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_idx = new_x * 3 + new_y
                new_state = state[:]
                new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
                neighbors.append(new_state)
        return neighbors

    def reconstruct_path(node):
        path = []
        while node.parent:
            path.append((node.depth, node.h, node.cost, node.state)) 
            node = node.parent
        path.reverse()
        return path

    open_set = []
    heapq.heappush(open_set, Node(initial_state, cost=manhattan_distance(initial_state, goal_state), h=manhattan_distance(initial_state, goal_state)))
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            return reconstruct_path(current_node), current_node.depth

        closed_set.add(tuple(current_node.state))

        for neighbor in get_neighbors(current_node.state):
            if tuple(neighbor) in closed_set:
                continue

            g = current_node.depth + 1  
            h_value = manhattan_distance(neighbor, goal_state)  
            f = g + h_value  

            neighbor_node = Node(state=neighbor, parent=current_node, depth=g, cost=f, h=h_value)
            heapq.heappush(open_set, neighbor_node)

    return None, -1

path, depth = astar_manhattan(initial_state, goal_state)
print(f"Number of moves: {depth}\n")

print("Initial state:")
print_puzzle(initial_state)

for g, h, f, state in path:
    print(f"g(n) = {g}, h(n) = {h}, f(n) = {f}")
    print_puzzle(state)

print("Goal state reached!")
