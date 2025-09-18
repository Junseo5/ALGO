# 2819 . 격자판의 숫자 이어 붙이기

def dfs(x, y, idx, num):
    if idx == 7:
        result_set.add(num)
        return

    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < SIZE and 0 <= ny < SIZE:
            dfs(nx, ny, idx + 1, num + board[nx][ny])


SIZE = 4
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

tc = int(input())

for T in range(tc):
    board = [input().split() for _ in range(SIZE)]

    result_set = set()

    for i in range(SIZE):
        for j in range(SIZE):
            dfs(i, j, 1, board[i][j])

    print(f"#{T + 1} {len(result_set)}")