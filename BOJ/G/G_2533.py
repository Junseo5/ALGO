# Gold 3 . 사회망 서비스(SNS)

# 프림 형식으로 & 붙어있는 노드 개수를 가중치로

from collections import defaultdict
import heapq

N = int(input())

N_dict = defaultdict(list)
for i in range(N - 1):
    u, v = map(int, input().split())
    N_dict[u].append(v)
    N_dict[v].append(u)

pq = []
for i in range(1, N + 1):
    if len(N_dict[i]) == 1:
        heapq.heappush(pq, (len(N_dict[i]), i))

visited = set()
ea = set()  # 얼리 아답터
while pq:
    w, u = heapq.heappop(pq)

    if u in visited:
        continue
    visited.add(u)

    for v in N_dict[u]:
        if u not in ea and v not in ea:
            ea.add(v)
        if v not in visited:
            heapq.heappush(pq, (len(N_dict[v]), v))

print(len(ea))