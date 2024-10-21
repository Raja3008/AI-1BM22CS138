import heapq

def misplaced_tiles(state, goal):
    """Calculate the number of misplaced tiles."""
    return sum(1 for i in range(9) if state[i] != goal[i] and state[i] != 0)

class Node:
    def __init__(self, state, parent=None, depth=0, cost=0, h=0):
        self.state = state
        self.parent = parent
        self.depth = depth 
        self.cost = cost  
        self.h = h  

    def __lt__(self, other):
        return self.cost < other.cost

def astar_misplaced(initial_state, goal_state):
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
    heapq.heappush(open_set, Node(initial_state, cost=misplaced_tiles(initial_state, goal_state), h=misplaced_tiles(initial_state, goal_state)))
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
            h_value = misplaced_tiles(neighbor, goal_state)
            f = g + h_value

            neighbor_node = Node(state=neighbor, parent=current_node, depth=g, cost=f, h=h_value)
            heapq.heappush(open_set, neighbor_node)

    return None, -1

def print_puzzle(state):
    print(f"{state[0]} {state[1]} {state[2]}")
    print(f"{state[3]} {state[4]} {state[5]}")
    print(f"{state[6]} {state[7]} {state[8]}")
    print()

initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

path, depth = astar_misplaced(initial_state, goal_state)
print(f"Number of moves: {depth}\n")

print("Initial state:")
print_puzzle(initial_state)

for g, h, f, state in path:
    print(f"g(n) = {g}, h(n) = {h}, f(n) = {f}")
    print_puzzle(state)

print("Goal state reached!")
