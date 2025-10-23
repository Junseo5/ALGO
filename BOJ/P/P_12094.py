# Platinum 3 . 2048 (Hard)

from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_value = 0

def move_left(board):
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        queue = deque()
        for j in range(N):
            if board[i][j]:
                queue.append(board[i][j])
        row = [0] * N
        idx = 0
        while queue:
            val = queue.popleft()
            if row[idx] == 0:
                row[idx] = val
            elif row[idx] == val:
                row[idx] *= 2
                idx += 1
            else:
                idx += 1
                row[idx] = val
        new_board[i] = row
    return new_board

def rotate(board):
    return [list(row) for row in zip(*board[::-1])]

def get_max(board):
    return max(max(row) for row in board)

def dfs(board, depth):
    global max_value
    if depth == 10:
        max_value = max(max_value, get_max(board))
        return
    for _ in range(4):
        new_board = move_left(board)
        if new_board != board:
            dfs(new_board, depth + 1)
        board = rotate(board)

dfs(board, 0)
print(max_value)
