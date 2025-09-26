# 5293 . 이진 문자열 복원

def build(a, b, c, d):
    total_edges = a + b + c + d

    # Eulerian path 조건 체크
    if abs(b - c) > 1:
        return ''
    if a > 0 and b == 0 and c == 0 and d > 0:
        return ''

    # 인접 행렬 (간선 개수 저장)
    adj = {0: {0: a, 1: b}, 1: {0: c, 1: d}}

    # 시작점 결정
    if b - c == 1:
        start = 0
    elif c - b == 1:
        start = 1
    else:
        if a + b > 0:
            start = 0
        elif c + d > 0:
            start = 1
        else:
            return "0"

    # Hierholzer 알고리즘
    stack = [start]
    path = []
    while stack:
        u = stack[-1]
        if adj[u][0] > 0:
            adj[u][0] -= 1
            stack.append(0)
        elif adj[u][1] > 0:
            adj[u][1] -= 1
            stack.append(1)
        else:
            path.append(stack.pop())

    path.reverse()
    if len(path) != total_edges + 1:
        return ''

    return ''.join(str(x) for x in path)


result_list = []
tc = int(input())

for T in range(tc):
    a, b, c, d = map(int, input().split())
    result = build(a, b, c, d)

    if not result:
        result = 'impossible'

    result_list.append(f"#{T + 1} {result}\n")

print(''.join(result_list))





# def dfs(graph, start, visited=None, result_str=''):
#     global result
#     if visited is None:
#         visited = set()
#         result_str = graph[start]
#
#     visited.add(start)
#
#     if result_len == len(result_str):
#         result = result_str
#         return True
#
#     for i, v in enumerate(graph):
#         if i not in visited:
#             if result_str[-1] == v[0]:
#                 if dfs(graph, i, visited, result_str + v[1]):
#                     return True
#
#     visited.remove(start)
#     return False
#
#
# result_list = []
# tc = int(input())
#
# for T in range(tc):
#     # a: 00, b: 01, c: 10, d: 11
#     a, b, c, d = map(int, input().split())
#     n_list = ['00']*a + ['01']*b + ['10']*c + ['11']*d
#     result_len = a + b + c + d + 1
#
#     result = ''
#     sames = set()
#     if a > 0 and b == 0 and c == 0 and d > 0:
#         pass
#     else:
#         for i in range(len(n_list)):
#             if result:
#                 break
#             if n_list[i] in sames:
#                 continue
#             if dfs(n_list, i):
#                 break
#             sames.add(n_list[i])
#
#     if not result:
#         result = 'impossible'
#
#     result_list.append(f"#{T + 1} {result}\n")
#
# print(''.join(result_list))