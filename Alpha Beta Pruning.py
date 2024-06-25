import math


def evaluate(board):
    # Example evaluation function for Tic-Tac-Toe
    # Returns +1 if the maximizer (X) wins, -1 if the minimizer (O) wins, 0 for a draw
    # You would need to customize this for different games and board states
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    else:
        return 0


def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    # Assume board is represented as a 3x3 list
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]

    for condition in win_conditions:
        if all(cell == player for cell in condition):
            return True
    return False


def is_terminal(board):
    # Check if the board is in a terminal state (win or draw)
    return check_winner(board, 'X') or check_winner(board, 'O') or all(
        all(cell != '-' for cell in row) for row in board)


def minimax_alpha_beta(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or is_terminal(board):
        return evaluate(board)

    if maximizingPlayer:
        maxEval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    eval = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
                    board[i][j] = '-'
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return maxEval
    else:
        minEval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    eval = minimax_alpha_beta(board, depth - 1, alpha, beta, True)
                    board[i][j] = '-'
                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return minEval


def find_best_move(board):
    bestVal = -math.inf
    bestMove = None
    alpha = -math.inf
    beta = math.inf

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                moveVal = minimax_alpha_beta(board, 3, alpha, beta, False)
                board[i][j] = '-'

                if moveVal > bestVal:
                    bestVal = moveVal
                    bestMove = (i, j)

    return bestMove


def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


# Function to initialize the board based on user input
def initialize_board():
    print("Enter the initial state of the board:")
    board = [['-' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            while True:
                user_input = input(f"Enter value for board[{i}][{j}] ('X', 'O', or '-'): ").strip().upper()
                if user_input in ['X', 'O', '-']:
                    board[i][j] = user_input
                    break
                else:
                    print("Invalid input! Please enter 'X', 'O', or '-'")
    return board


# Example usage where user provides initial state and shows the best move for 'X'
def main():
    # Initialize the board based on user input
    board = initialize_board()

    print("\nInitial Board:")
    print_board(board)

    # Find and print the best move for 'X' using the minimax algorithm with alpha-beta pruning
    best_move = find_best_move(board)
    print("Best move for 'X':", best_move)


if __name__ == "__main__":
    main()
