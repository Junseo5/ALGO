# Gold 3 . 사회망 서비스(SNS)

from collections import defaultdict

# 입력 받기
N = int(input())
graph = [[] for _ in range(N + 1)]
dp = [[-1, -1] for _ in range(N + 1)]  # dp[u][0]과 dp[u][1]을 저장

# 트리 구성
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS + DP 함수
def dfs(node, parent):
    dp[node][0] = 0  # 부모가 얼리 아답터가 아니면 자식은 얼리 아답터여야 함
    dp[node][1] = 1  # 부모가 얼리 아답터이면 자식은 안 해도 됨

    for child in graph[node]:
        if child == parent:
            continue

        dfs(child, node)

        # dp[node][0]은 자식이 모두 얼리 아답터일 때의 값
        dp[node][0] += dp[child][1]
        # dp[node][1]은 자식이 얼리 아답터일 필요 없으므로 둘 중 더 작은 값
        dp[node][1] += min(dp[child][0], dp[child][1])

# 트리의 루트(1번 노드부터 DFS 시작)
dfs(1, -1)

# 루트에서 얼리 아답터가 될 수 있는 최소값을 출력
print(min(dp[1][0], dp[1][1]))




# # 프림 형식으로 & 붙어있는 노드 개수를 가중치로
#
# from collections import defaultdict
# import heapq
#
# N = int(input())
#
# N_dict = defaultdict(list)
# for i in range(N - 1):
#     u, v = map(int, input().split())
#     N_dict[u].append(v)
#     N_dict[v].append(u)
#
# pq = []
# for i in range(1, N + 1):
#     if len(N_dict[i]) == 1:
#         heapq.heappush(pq, (len(N_dict[i]), i))
#
# visited = set()
# ea = set()  # 얼리 아답터
# while pq:
#     w, u = heapq.heappop(pq)
#
#     if u in visited:
#         continue
#     visited.add(u)
#
#     for v in N_dict[u]:
#         if u not in ea and v not in ea:
#             ea.add(v)
#         if v not in visited:
#             heapq.heappush(pq, (len(N_dict[v]), v))
#
# print(len(ea))