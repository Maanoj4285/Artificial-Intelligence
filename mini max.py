import math

# Constants for representing the players and empty spots on the board
EMPTY = 0
PLAYER_X = 1
PLAYER_O = -1


# Evaluation function (utility function) for Tic-Tac-Toe
def evaluate(board):
    # Check rows, columns, and diagonals for win/lose/draw conditions
    for row in board:
        if all([cell == PLAYER_X for cell in row]):
            return 1  # Player X wins
        elif all([cell == PLAYER_O for cell in row]):
            return -1  # Player O wins

    for col in range(3):
        if all([board[row][col] == PLAYER_X for row in range(3)]):
            return 1  # Player X wins
        elif all([board[row][col] == PLAYER_O for row in range(3)]):
            return -1  # Player O wins

    if all([board[i][i] == PLAYER_X for i in range(3)]) or all([board[i][2 - i] == PLAYER_X for i in range(3)]):
        return 1  # Player X wins
    elif all([board[i][i] == PLAYER_O for i in range(3)]) or all([board[i][2 - i] == PLAYER_O for i in range(3)]):
        return -1  # Player O wins

    # Check if the board is full (draw condition)
    if all([cell != EMPTY for row in board for cell in row]):
        return 0  # Draw

    # Game is not over yet
    return None


# Minimax algorithm function with print for debugging the tree
def minimax(board, depth, is_maximizing):
    result = evaluate(board)

    # If the game is over, return the evaluation score
    if result is not None:
        return result

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    # Try this move for the maximizing player
                    board[row][col] = PLAYER_X
                    score = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY  # Undo the move
                    best_score = max(score, best_score)
                    # Print the minimax tree
                    if depth == 0:
                        print(f"Move: ({row}, {col}) Score: {score}")
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    # Try this move for the minimizing player
                    board[row][col] = PLAYER_O
                    score = minimax(board, depth + 1, True)
                    board[row][col] = EMPTY  # Undo the move
                    best_score = min(score, best_score)
                    # Print the minimax tree
                    if depth == 0:
                        print(f"Move: ({row}, {col}) Score: {score}")
        return best_score


# Function to print the current board state
def print_board(board):
    for row in board:
        print(row)


# Example usage for Tic-Tac-Toe
if __name__ == "__main__":
    board = []

    print("Enter the initial state of the board (1 for X, -1 for O, 0 for empty):")
    for i in range(3):
        row = list(map(int, input().split()))
        board.append(row)

    print("\nInitial board:")
    print_board(board)

    # Prompt the user for the next move (X or O)
    next_move = int(input("Enter next move (1 for X, -1 for O): "))
    if next_move == 1:
        is_maximizing = True
    else:
        is_maximizing = False

    print("\nMiniMax Decision Tree:")
    score = minimax(board, 0, is_maximizing)

    if score == 1:
        print("\nPlayer X wins!")
    elif score == -1:
        print("\nPlayer O wins!")
    else:
        print("\nIt's a draw!")
