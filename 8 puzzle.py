import heapq


class Puzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.dimension = int(len(start) ** 0.5)

    def get_neighbors(self, state):
        neighbors = []
        blank_index = state.index(0)
        row, col = divmod(blank_index, self.dimension)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.dimension and 0 <= new_col < self.dimension:
                new_blank_index = new_row * self.dimension + new_col
                new_state = list(state)
                new_state[blank_index], new_state[new_blank_index] = new_state[new_blank_index], new_state[blank_index]
                neighbors.append(tuple(new_state))

        return neighbors

    def heuristic(self, state):
        distance = 0
        for i, value in enumerate(state):
            if value != 0:
                goal_index = self.goal.index(value)
                current_row, current_col = divmod(i, self.dimension)
                goal_row, goal_col = divmod(goal_index, self.dimension)
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

    def a_star(self):
        start_tuple = tuple(self.start)
        goal_tuple = tuple(self.goal)

        open_set = []
        heapq.heappush(open_set, (self.heuristic(start_tuple), start_tuple))
        came_from = {start_tuple: None}
        g_score = {start_tuple: 0}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal_tuple:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor)
                    heapq.heappush(open_set, (f_score, neighbor))

        return None

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from and came_from[current] is not None:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path


# Example usage:
start = [5, 4, 0, 6, 1, 8, 7, 3, 2]
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

puzzle = Puzzle(start, goal)
solution = puzzle.a_star()

if solution:
    count = 0
    for step in solution:
        print(step)
        count += 1
    print("Number of steps: ", count)

else:
    print("No solution found.")
