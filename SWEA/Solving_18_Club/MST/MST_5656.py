# 5656 . [모의 SW 역량테스트] 벽돌 깨기

from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def boom(board, x, y, H, W):
    if board[x][y] == 0:
        return
    q = deque()
    q.append((x, y, board[x][y]))
    board[x][y] = 0

    while q:
        x, y, power = q.popleft()
        for d in range(4):
            for step in range(1, power):
                nx, ny = x + dx[d]*step, y + dy[d]*step
                if 0 <= nx < H and 0 <= ny < W and board[nx][ny] != 0:
                    q.append((nx, ny, board[nx][ny]))
                    board[nx][ny] = 0

def drop(board, H, W):
    for j in range(W):
        stack = []
        for i in range(H-1, -1, -1):
            if board[i][j] != 0:
                stack.append(board[i][j])
        for i in range(H-1, -1, -1):
            if stack:
                board[i][j] = stack.pop(0)
            else:
                board[i][j] = 0

def count_bricks(board):
    return sum(1 for row in board for val in row if val != 0)

def dfs(depth, N, board, H, W):
    if depth == N:
        return count_bricks(board)

    min_bricks = float('inf')
    for col in range(W):
        row = -1
        for i in range(H):
            if board[i][col] != 0:
                row = i
                break

        if row == -1:
            continue

        new_board = copy.deepcopy(board)
        boom(new_board, row, col, H, W)
        drop(new_board, H, W)
        min_bricks = min(min_bricks, dfs(depth+1, N, new_board, H, W))

    return min_bricks

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    result = dfs(0, N, board, H, W)
    print(f"#{tc} {result if result != float('inf') else 0}")
