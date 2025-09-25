# 5251 . [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리

from collections import defaultdict
import heapq

tc = int(input())

for T in range(tc):
    n, e = map(int, input().split())
    n_list = [i for i in range(n + 1)]
    base_list = [0] + [float('inf')] * n

    n_dict = defaultdict(list)
    for i in range(e):
        u, v, w = map(int, input().split())
        n_dict[u].append((v, w))

    pq = []
    heapq.heappush(pq, (0, 0))
    while pq:
        temp_total_w, u = heapq.heappop(pq)

        if u == n: break

        if base_list[u] < temp_total_w: continue

        for v, w in n_dict[u]:
            total_w = temp_total_w + w
            if base_list[v] > total_w:
                base_list[v] = total_w
                heapq.heappush(pq, (total_w, v))

    print(f"#{T + 1} {base_list[-1]}")