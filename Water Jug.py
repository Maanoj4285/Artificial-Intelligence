from collections import deque


def water_jug_solver(jug1_capacity, jug2_capacity, target_jug1, target_jug2):
    # Initialize the BFS queue and a set for visited states
    queue = deque([((0, 0), [])])
    visited = set((0, 0))

    # Dictionary to store the path
    parent = {}
    parent[(0, 0)] = None

    while queue:
        # Get the current state and the actions taken to reach here
        (current_jug1, current_jug2), actions = queue.popleft()

        # Check if we have reached the target
        if current_jug1 == target_jug1 and current_jug2 == target_jug2:
            return actions  # Return the list of actions

        # List of possible next states
        next_states = []

        # Fill Jug 1
        next_states.append(((jug1_capacity, current_jug2), actions + [(current_jug1, current_jug2, "Fill Jug 1")]))
        # Fill Jug 2
        next_states.append(((current_jug1, jug2_capacity), actions + [(current_jug1, current_jug2, "Fill Jug 2")]))
        # Empty Jug 1
        next_states.append(((0, current_jug2), actions + [(current_jug1, current_jug2, "Empty Jug 1")]))
        # Empty Jug 2
        next_states.append(((current_jug1, 0), actions + [(current_jug1, current_jug2, "Empty Jug 2")]))
        # Pour Jug 1 to Jug 2
        pour_to_jug2 = min(current_jug1, jug2_capacity - current_jug2)
        next_states.append(((current_jug1 - pour_to_jug2, current_jug2 + pour_to_jug2),
                            actions + [(current_jug1, current_jug2, f"Pour {pour_to_jug2} units from Jug 1 to Jug 2")]))
        # Pour Jug 2 to Jug 1
        pour_to_jug1 = min(current_jug2, jug1_capacity - current_jug1)
        next_states.append(((current_jug1 + pour_to_jug1, current_jug2 - pour_to_jug1),
                            actions + [(current_jug1, current_jug2, f"Pour {pour_to_jug1} units from Jug 2 to Jug 1")]))

        for state, new_actions in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, new_actions))
                parent[state] = (current_jug1, current_jug2)

    return None  # No solution found


def get_user_input():
    jug1_capacity = int(input("Enter the capacity of Jug 1: "))
    jug2_capacity = int(input("Enter the capacity of Jug 2: "))
    target_jug1 = int(input("Enter the desired amount in Jug 1: "))
    target_jug2 = int(input("Enter the desired amount in Jug 2: "))
    return jug1_capacity, jug2_capacity, target_jug1, target_jug2


# Example usage with user input
print("Enter the capacities and desired amounts for the Water Jug Problem:")
jug1_capacity, jug2_capacity, target_jug1, target_jug2 = get_user_input()

solution = water_jug_solver(jug1_capacity, jug2_capacity, target_jug1, target_jug2)
if solution:
    print("Solution steps:")
    for step in solution:
        current_state, action = step[:-1], step[-1]
        print(f"Action: {action}")
        print(f"Current state: Jug 1 has {current_state[0]} units, Jug 2 has {current_state[1]} units")
        print()
else:
    print("No solution exists.")
