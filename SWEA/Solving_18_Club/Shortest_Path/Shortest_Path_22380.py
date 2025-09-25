# 22380 . 경민이의 기차 여행

from collections import defaultdict
import heapq

tc = int(input())

for T in range(tc):
    n, e = map(int, input().split())
    n_list = [i for i in range(n)]
    memo = [0] + [float('inf')] * (n - 1)

    n_dict = defaultdict(list)
    for i in range(e):
        a, b, w = map(int, input().split())
        n_dict[a].append((b, w))

    pq = []
    heapq.heappush(pq, (0, 0))
    while pq:
        temp_total_w, u = heapq.heappop(pq)

        if u == n - 1: break

        for v, w in n_dict[u]:
            total_w = temp_total_w + w
            if memo[v] > total_w:
                memo[v] = total_w
                heapq.heappush(pq, (total_w, v))

    result = str(memo[-1])
    if memo[-1] == float('inf'):
        result = 'impossible'

    print(f"#{T + 1} {result}")