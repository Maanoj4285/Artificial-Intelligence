def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")


def is_safe(board, row, col):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens_util(board, col):
    # If all queens are placed then return true
    if col >= len(board):
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 'Q'

            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = '.'

    # If the queen cannot be placed in any row in this column, return false
    return False


def solve_n_queens_with_input():
    # Initialize an 8x8 board with all empty spaces
    board = [['.' for _ in range(8)] for _ in range(8)]

    # Take user input for the initial positions
    initial_positions = []
    for _ in range(8):
        pos = input("Enter the position of a queen (row and column) separated by a space: ").split()
        row, col = int(pos[0]), int(pos[1])
        initial_positions.append((row, col))

    # Place the initial queens on the board
    for pos in initial_positions:
        row, col = pos
        board[row][col] = 'Q'

    print("Initial board:")
    print_board(board)

    # Check for unsafe positions
    for row, col in initial_positions:
        if not is_safe(board, row, col):
            print(f"Queen at ({row}, {col}) is in an unsafe position.")
        else:
            print(f"Queen at ({row}, {col}) is in a safe position.")

    # Remove all queens to attempt solving from scratch
    for row, col in initial_positions:
        board[row][col] = '.'

    # Solve the 8 queens problem
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False

    print("Final board:")
    print_board(board)
    return True


# Call the function to solve the problem with user input
solve_n_queens_with_input()
