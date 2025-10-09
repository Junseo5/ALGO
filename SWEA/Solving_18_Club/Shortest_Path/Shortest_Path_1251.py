# 1251 . [S/W 문제해결 응용] 4일차 - 하나로

import heapq

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    E = float(input())

    visited = [False] * N
    min_edge = [float('inf')] * N  # 각 노드에 연결되는 최소 거리
    min_edge[0] = 0  # 시작점은 0 비용으로 시작
    pq = [(0, 0)]  # (비용, 노드)
    total_cost = 0

    while pq:
        cost, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost  # 이 간선을 MST에 포함

        # 인접 노드(모든 섬) 갱신
        for v in range(N):
            if not visited[v]:
                dist_sq = (x[u] - x[v]) ** 2 + (y[u] - y[v]) ** 2
                if dist_sq < min_edge[v]:
                    min_edge[v] = dist_sq
                    heapq.heappush(pq, (dist_sq, v))

    # 환경 부담금 계산
    result = total_cost * E
    print(f"#{tc} {round(result)}")