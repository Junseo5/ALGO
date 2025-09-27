# 5719. 거의 최단 경로

from collections import defaultdict, deque
import heapq

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    s, d = map(int, input().split())
    m_dict = defaultdict(list)
    for _ in range(m):
        u, v, p = map(int, input().split())
        m_dict[u].append((v, p))

    memo = [float('inf')] * n
    parent = [[] for _ in range(n)]
    pq = []
    heapq.heappush(pq, (0, s))
    memo[s] = 0

    while pq:
        w, loc = heapq.heappop(pq)
        if w > memo[loc]:
            continue
        for v, p in m_dict[loc]:
            total_w = w + p
            if memo[v] > total_w:
                memo[v] = total_w
                parent[v] = [loc]
                heapq.heappush(pq, (total_w, v))
            elif memo[v] == total_w:
                parent[v].append(loc)

    if memo[d] == float('inf'):
        result = -1
        print(result)
        continue

    removed_edges = set()
    q = deque([d])
    visited = [False] * n
    while q:
        v = q.popleft()
        for u in parent[v]:
            removed_edges.add((u, v))
            if not visited[u]:
                visited[u] = True
                q.append(u)

    memo = [float('inf')] * n
    pq = []
    heapq.heappush(pq, (0, s))
    memo[s] = 0

    while pq:
        w, loc = heapq.heappop(pq)
        if w > memo[loc]:
            continue
        for v, p in m_dict[loc]:
            if (loc, v) in removed_edges:
                continue
            total_w = w + p
            if memo[v] > total_w:
                memo[v] = total_w
                heapq.heappush(pq, (total_w, v))

    if memo[d] == float('inf'):
        result = -1
    else:
        result = memo[d]

    print(result)
