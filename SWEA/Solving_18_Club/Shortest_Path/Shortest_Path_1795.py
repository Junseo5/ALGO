# 1795 . 인수의 생일 파티

from collections import defaultdict
import heapq


def dijkstra(s, e):
    base_list = [0] + [float('inf')] * n
    pq = []
    heapq.heappush(pq, (0, s))
    while pq:
        temp_total_w, u = heapq.heappop(pq)

        if u == e: break

        if base_list[u] < temp_total_w: continue

        for v, w in n_dict[u]:
            total_w = temp_total_w + w
            if base_list[v] > total_w:
                base_list[v] = total_w
                heapq.heappush(pq, (total_w, v))

    return base_list[e]


tc = int(input())

for T in range(tc):
    n, m, x = map(int, input().split())
    n_list = [i for i in range(n + 1)]

    n_dict = defaultdict(list)
    for i in range(m):
        a, b, c = map(int, input().split())
        n_dict[a].append((b, c))

    max_distance = 0
    for i in range(1, n + 1):
        if i == x: continue

        distance1 = dijkstra(i, x)
        distance2 = dijkstra(x, i)

        max_distance = max(max_distance, distance1 + distance2)

    print(f"#{T + 1} {max_distance}")