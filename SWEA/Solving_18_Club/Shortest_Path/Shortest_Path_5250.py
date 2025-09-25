# 5250 . [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용

import heapq

tc = int(input())

for T in range(tc):
    n = int(input())
    n_list = [list(map(int, input().split())) for _ in range(n)]
    base_list = [[float('inf')] * n for _ in range(n)]
    base_list[0][0] = 0

    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    pq = []
    heapq.heappush(pq, (0, 0, 0))
    while pq:
        temp_total_w, x, y = heapq.heappop(pq)

        if (x, y) == (n-1, n-1): break

        if base_list[x][y] < temp_total_w: continue

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                temp_op = n_list[nx][ny] - n_list[x][y]
                if temp_op < 0:
                    temp_op = 0

                total_w = temp_total_w + (1 + temp_op)
                if base_list[nx][ny] > total_w:
                    base_list[nx][ny] = total_w
                    heapq.heappush(pq, (total_w, nx, ny))

    print(f"#{T + 1} {base_list[n-1][n-1]}")