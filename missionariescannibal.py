from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, depth=0):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.depth = depth
        self.parent = None  # To store parent state

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or \
           self.missionaries > 3 or self.cannibals > 3:
            return False
        
        if (self.missionaries > 0 and self.missionaries < self.cannibals) or \
           (3 - self.missionaries > 0 and 3 - self.missionaries < 3 - self.cannibals):
            return False
        
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return self.missionaries == other.missionaries and \
               self.cannibals == other.cannibals and \
               self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def get_successors(state):
    successors = []
    
    if state.boat == 1:  # Boat is on the original side
        possible_moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for move in possible_moves:
            new_state = State(state.missionaries - move[0], state.cannibals - move[1], 0, state.depth + 1)
            if new_state.is_valid():
                new_state.parent = state  # Set parent state
                successors.append(new_state)
    else:  # Boat is on the other side
        possible_moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        for move in possible_moves:
            new_state = State(state.missionaries + move[0], state.cannibals + move[1], 1, state.depth + 1)
            if new_state.is_valid():
                new_state.parent = state  # Set parent state
                successors.append(new_state)
    
    return successors

def bfs():
    initial_state = State(3, 3, 1)
    
    if initial_state.is_goal():
        return initial_state
    
    frontier = deque([initial_state])
    explored = set()
    
    while frontier:
        state = frontier.popleft()
        
        if state.is_goal():
            return state
        
        explored.add(state)
        
        for successor in get_successors(state):
            if successor not in explored and successor not in frontier:
                frontier.append(successor)
    
    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
        return
    
    path = []
    while solution:
        path.append(solution)
        solution = solution.parent
    
    path.reverse()
    for state in path:
        print(f"Missionaries: {state.missionaries}, Cannibals: {state.cannibals}, Boat: {state.boat}")

def main():
    solution = bfs()
    print_solution(solution)

if __name__ == "__main__":
    main()
