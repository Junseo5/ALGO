# 1226 . [S/W 문제해결 기본] 7일차 - 미로1

size = 16
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def dfs(graph, loc_idx):
    global result
    loc_dx, loc_dy = loc_idx

    if result == '1' or graph[loc_dx][loc_dy] == 3:
        result = '1'
        return

    graph[loc_dx][loc_dy] = 5

    for dx, dy in dxdy:
        x = loc_dx + dx
        y = loc_dy + dy
        if 0 <= x < size and 0 <= y < size:
            if result == '1' or graph[x][y] == 3:
                result = '1'
                return
            if graph[x][y] == 0:
                dfs(graph, (x, y))


for T in range(10):
    input()
    board = [list(map(int, list(input()))) for _ in range(size)]

    result = '0'
    start_idx = (1, 1)

    dfs(board, start_idx)

    print(f"#{T + 1} {result}")