# 1226 . [S/W 문제해결 기본] 7일차 - 미로1

from collections import deque

size = 16
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(graph, start):
    visited = [[False] * size for _ in range(size)]
    dq = deque([start])
    visited[start[0]][start[1]] = True

    while dq:
        x, y = dq.popleft()

        if graph[x][y] == 3:
            return '1'

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size:
                if not visited[nx][ny] and (graph[nx][ny] == 0 or graph[nx][ny] == 3):
                    visited[nx][ny] = True
                    dq.append((nx, ny))

    return '0'


for T in range(10):
    input()
    board = [list(map(int, list(input().strip()))) for _ in range(size)]

    start_idx = (1, 1)
    result = bfs(board, start_idx)

    print(f"#{T + 1} {result}")
