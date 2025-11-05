def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row,n), range(col,-1,-1)):
        if board[i][j]:
            return False
    return True

def solve(board, col, n):
    if col == n:
        print_board(board)
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve(board, col+1, n)
            board[i][col] = 0

# Example (first queen already placed at [0][0])
n = 4
board = [[0]*n for _ in range(n)]
board[0][0] = 1
solve(board, 1, n)
