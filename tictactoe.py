import math

# Constants for the players
HUMAN = -1
AI = 1

# Function to evaluate the board state
def evaluate(board):
    if wins(board, AI):
        score = 1
    elif wins(board, HUMAN):
        score = -1
    else:
        score = 0
    return score

# Function to check if a player has won
def wins(board, player):
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_states

# Function to check for empty cells on the board
def empty_cells(board):
    cells = []
    for x, row in enumerate(board):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])
    return cells

# Function to check if the game is over
def game_over(board):
    return wins(board, HUMAN) or wins(board, AI)

# Minimax function
def minimax(board, depth, player):
    if player == AI:
        best = [-1, -1, -math.inf]
    else:
        best = [-1, -1, math.inf]

    if depth == 0 or game_over(board):
        score = evaluate(board)
        return [-1, -1, score]

    for cell in empty_cells(board):
        x, y = cell
        board[x][y] = player
        score = minimax(board, depth - 1, -player)
        board[x][y] = 0
        score[0], score[1] = x, y

        if player == AI:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best

# Function to make the best move
def ai_turn(board):
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    move = minimax(board, depth, AI)
    x, y = move[0], move[1]
    board[x][y] = AI

# Function to print the board
def print_board(board):
    chars = {HUMAN: 'X', AI: 'O', 0: ' '}
    for row in board:
        print('|'.join([chars[cell] for cell in row]))
        print('-----')

# Main function to run the game
def main():
    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    human_turn = True

    while len(empty_cells(board)) > 0 and not game_over(board):
        print_board(board)
        if human_turn:
            x = int(input("Enter the row (0, 1, 2): "))
            y = int(input("Enter the column (0, 1, 2): "))
            if board[x][y] == 0:
                board[x][y] = HUMAN
                human_turn = False
        else:
            ai_turn(board)
            human_turn = True

    print_board(board)

    if wins(board, HUMAN):
        print("You win!")
    elif wins(board, AI):
        print("AI wins!")
    else:
        print("Draw!")

if __name__ == "__main__":
    main()
