class Game:
    def __init__(self):
        pass

    def is_terminal(self, state):
        # Implement this method to check if the game has reached a terminal state
        pass

    def get_possible_moves(self, state, player):
        # Implement this method to get all possible moves for the current player
        pass

    def make_move(self, state, move, player):
        # Implement this method to apply a move and return the new state
        pass

    def evaluate(self, state):
        # Implement this method to evaluate the given state
        pass

def alpha_beta_pruning(game, state, depth, alpha, beta, maximizing_player):
    if depth == 0 or game.is_terminal(state):
        return game.evaluate(state)

    if maximizing_player:
        max_eval = float('-inf')
        for move in game.get_possible_moves(state, True):
            new_state = game.make_move(state, move, True)
            eval = alpha_beta_pruning(game, new_state, depth-1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in game.get_possible_moves(state, False):
            new_state = game.make_move(state, move, False)
            eval = alpha_beta_pruning(game, new_state, depth-1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Example usage (tic-tac-toe, chess, etc.)
class TicTacToe(Game):
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def is_terminal(self, state):
        # Define terminal condition: win or draw
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condition in win_conditions:
            if state[condition[0]] == state[condition[1]] == state[condition[2]] != ' ':
                return True
        return ' ' not in state

    def get_possible_moves(self, state, player):
        # Return all empty positions
        return [i for i, cell in enumerate(state) if cell == ' ']

    def make_move(self, state, move, player):
        new_state = state[:]
        new_state[move] = 'X' if player else 'O'
        return new_state

    def evaluate(self, state):
        # Evaluation logic: +1 for X win, -1 for O win, 0 for draw
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condition in win_conditions:
            if state[condition[0]] == state[condition[1]] == state[condition[2]] != ' ':
                return 1 if state[condition[0]] == 'X' else -1
        return 0

# Example usage
game = TicTacToe()
initial_state = game.board
depth = 9  # maximum depth for tic-tac-toe
maximizing_player = True

best_score = alpha_beta_pruning(game, initial_state, depth, float('-inf'), float('inf'), maximizing_player)
print("Best score for the starting player (X):", best_score)
