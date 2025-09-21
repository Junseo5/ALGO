# 1249 . [S/W 문제해결 응용] 4일차 - 보급로

import heapq

tc = int(input().strip())

for T in range(tc):
    n = int(input().strip())
    n_list = [list(map(int, list(input().strip()))) for _ in range(n)]

    base_list = [[float('inf')] * n for _ in range(n)]
    base_list[0][0] = 0
    hq = []
    heapq.heappush(hq, (0, 0, 0))

    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while hq:
        score, x, y = heapq.heappop(hq)

        if (x, y) == (n-1, n-1):
            break

        if score > base_list[x][y]:
            continue

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                n_score = score + n_list[nx][ny]
                if n_score < base_list[nx][ny]:
                    base_list[nx][ny] = n_score
                    heapq.heappush(hq, (n_score, nx, ny))

    print(f"#{T + 1} {base_list[n-1][n-1]}")