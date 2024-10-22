import random

def calculate_attacking_pairs(state):
    attacking_pairs = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacking_pairs += 1
    return attacking_pairs

def get_neighbors(state):
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                new_state = list(state)
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors

def hill_climbing(n, max_iterations=1000):
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_attacking_pairs = calculate_attacking_pairs(current_state)

    for iteration in range(max_iterations):
        if current_attacking_pairs == 0:
            return current_state

        neighbors = get_neighbors(current_state)
        neighbor_attacking_pairs = [(neighbor, calculate_attacking_pairs(neighbor)) for neighbor in neighbors]
        next_state, next_attacking_pairs = min(neighbor_attacking_pairs, key=lambda x: x[1])

        if next_attacking_pairs >= current_attacking_pairs:
            print(f"Local maximum reached  {iteration}. ")
            return None

        current_state, current_attacking_pairs = next_state, next_attacking_pairs
        print(f" Current state: {current_state}, Attacking pairs: {current_attacking_pairs}")

    print(f"Max iterations reached without finding a solution.")
    return None

try:
    n = int(input("Enter the number of queens (N): "))
    if n <= 0:
        raise ValueError("N must be a positive integer.")
except ValueError as e:
    print(e)
    n = 4

solution = None

while solution is None:
    solution = hill_climbing(n)

print(f"Solution found: {solution}")
