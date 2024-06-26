from collections import deque

class VacuumCleanerState:
    def __init__(self, grid, position, path=None):
        self.grid = grid
        self.position = position
        self.path = path or []

    def is_goal(self):
        # Goal is achieved if all cells are cleaned
        return all(cell == 0 for row in self.grid for cell in row)

    def get_successors(self):
        successors = []
        x, y = self.position
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]):
                new_grid = [row[:] for row in self.grid]
                new_grid[x][y] = 0  # Clean current position
                new_position = (nx, ny)
                new_path = self.path + [new_position]
                successors.append(VacuumCleanerState(new_grid, new_position, new_path))

        return successors

def bfs_vacuum_cleaner(grid, start_position):
    initial_state = VacuumCleanerState(grid, start_position)
    if initial_state.is_goal():
        return initial_state.path

    frontier = deque([initial_state])
    explored = set()
    explored.add((initial_state.position, tuple(map(tuple, initial_state.grid))))

    while frontier:
        state = frontier.popleft()

        for successor in state.get_successors():
            grid_tuple = tuple(map(tuple, successor.grid))
            if (successor.position, grid_tuple) not in explored:
                if successor.is_goal():
                    return successor.path
                frontier.append(successor)
                explored.add((successor.position, grid_tuple))

    return None

def main():
    grid = [
        [1, 0, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    start_position = (0, 0)
    solution = bfs_vacuum_cleaner(grid, start_position)

    if solution:
        print("Solution path:", solution)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
