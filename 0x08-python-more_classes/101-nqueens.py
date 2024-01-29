#!/usr/bin/python3

from sys import argv


if __name__ == "__main__":
    chessboard = []

    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)

    board_size = int(argv[1])

    if board_size < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the chessboard as an empty NxN grid
    for row in range(board_size):
        chessboard.append([row, None])

    def is_queen_in_same_column(column):
        """Check if a queen already exists in the same column."""
        for row in range(board_size):
            if column == chessboard[row][1]:
                return True
        return False

    def does_attack_occur(row, column):
        """Determine whether or not the placement leads to an attack."""
        if is_queen_in_same_column(column):
            return False
        i = 0
        while i < row:
            if abs(chessboard[i][1] - column) == abs(i - row):
                return False
            i += 1
        return True

    def clear_board_from_current_row(row):
        """Clears the board from the point of failure onwards."""
        for i in range(row, board_size):
            chessboard[i][1] = None

    def solve_nqueens_recursive(row):
        """Recursive backtracking function to find the solution."""
        for column in range(board_size):
            clear_board_from_current_row(row)
            if does_attack_occur(row, column):
                chessboard[row][1] = column
                if row == board_size - 1:
                    print(chessboard)
                else:
                    solve_nqueens_recursive(row + 1)

    solve_nqueens_recursive(0)
