# 1249 . [S/W 문제해결 응용] 4일차 - 보급로

import heapq

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    n_list = [list(map(int, input().strip())) for _ in range(n)]
    base_list = [[float('inf')] * n for _ in range(n)]
    base_list[0][0] = 0

    dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    pq = []
    heapq.heappush(pq, (0, 0, 0))
    while pq:
        temp_total_w, x, y = heapq.heappop(pq)

        if (x, y) == (n-1, n-1): break

        if base_list[x][y] < temp_total_w: continue

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                total_w = temp_total_w + n_list[nx][ny]
                if base_list[nx][ny] > total_w:
                    base_list[nx][ny] = total_w
                    heapq.heappush(pq, (total_w, nx, ny))

    print(f"#{tc} {base_list[n-1][n-1]}")