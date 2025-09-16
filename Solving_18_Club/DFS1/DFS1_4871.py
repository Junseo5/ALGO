# 4871 . [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로

from collections import defaultdict


def dfs(graph, start, visited):
    visited.add(start)

    if end_node in visited:
        return

    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)


tc = int(input())

for T in range(tc):
    V, E = map(int, input().split())

    e_dict = defaultdict(list)
    for i in range(E):
        key, value = map(int, input().split())
        e_dict[key].append(value)

    start_node, end_node = map(int, input().split())

    visited_set = set()
    dfs(e_dict, start_node, visited_set)

    result = 0
    if end_node in visited_set:
        result = 1

    print(f"#{T + 1} {result}")