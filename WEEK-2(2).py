class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    def path(self):
        result = []
        current_node = self
        while current_node:
            result.append(current_node.state)
            current_node = current_node.parent
        return result[::-1] 


def iterative_deepening_search(problem):
    depth = 0
    while True:
        print(f"Exploring depth: {depth}")
        result, cutoff_occurred = depth_limited_search(problem, depth)
        if result is not None and not cutoff_occurred:
            return result  
        depth += 1  


def depth_limited_search(problem, limit):
    frontier = [Node(problem.initial_state)]
    explored = set()
    cutoff_occurred = False

    while frontier:
        node = frontier.pop()
        
        if problem.is_goal(node.state):
            return node.path(), False  

        if node.state not in explored:
            explored.add(node.state)
            if len(node.path()) - 1 < limit:
                for child in problem.expand(node.state):
                    frontier.append(Node(child, node))
            else:
                cutoff_occurred = True 
    return None, cutoff_occurred  


class GraphProblem:
    def __init__(self, initial_state, goal_state, adjacency_list):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.adjacency_list = adjacency_list

    def is_goal(self, state):
        return state == self.goal_state

    def expand(self, state):
        return self.adjacency_list.get(state, [])


def get_graph_from_input():
    adjacency_list = {}
    initial_state = input("Enter the initial state: ").strip()
    goal_state = input("Enter the goal state: ").strip()

    print("Enter the adjacency list for the graph ")
    print("Enter 'done' when finished.")

    while True:
        node = input("Enter node (or 'done' to stop): ").strip()
        if node.lower() == 'done':
            break
        neighbors_input = input(f"Enter the adjacent nodes of {node}: ").strip()
        neighbors = neighbors_input.split()
        adjacency_list[node] = [neighbor.strip() for neighbor in neighbors]

    return GraphProblem(initial_state, goal_state, adjacency_list)


if __name__ == "__main__":
    problem = get_graph_from_input()
    solution = iterative_deepening_search(problem)

    if solution:
        print("Solution Path:", solution)
    else:
        print("No solution found.")
