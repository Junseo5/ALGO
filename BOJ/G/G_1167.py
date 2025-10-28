# Gold 2 . 1167 트리의 지름

# 시간상 하드코딩 함수화 필요

from collections import defaultdict
import heapq

v_dict = defaultdict(list)

V = int(input())
for i in range(1, V + 1):
    v_list = list(map(int, input().split()))

    node = v_list[0]
    for j in range(1, len(v_list), 2):
        if len(v_list) - 2 > j:
            v_dict[node].append((v_list[j], v_list[j + 1]))
            v_dict[v_list[j]].append((node, v_list[j + 1]))

base_list = [float('inf')] * (V + 1)
pq = [(0, 1)]
visited = set()
base_list[1] = 0
while pq:
    temp_total_w, u = heapq.heappop(pq)

    if u in visited:
        continue
    visited.add(u)

    for v, w in v_dict[u]:
        total_w = temp_total_w + w
        if base_list[v] > total_w:
            base_list[v] = total_w
            heapq.heappush(pq, (total_w, v))

idx = base_list.index(max(base_list[1:]))

base_list = [float('inf')] * (V + 1)
pq = [(0, idx)]
visited = set()
heapq.heapify(pq)
base_list[idx] = 0
while pq:
    temp_total_w, u = heapq.heappop(pq)

    if u in visited:
        continue
    visited.add(u)

    for v, w in v_dict[u]:
        total_w = temp_total_w + w
        if base_list[v] > total_w:
            base_list[v] = total_w
            heapq.heappush(pq, (total_w, v))

print(max(base_list[1:]))