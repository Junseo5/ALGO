# 5174 . [파이썬 S/W 문제해결 기본] 8일차 - subtree

from collections import defaultdict


def node_counter(node, result):
    result.append(node)
    if len(node_dict[node]) == 2:
        node_counter(node_dict[node][0], result)
        node_counter(node_dict[node][1], result)
    elif len(node_dict[node]) == 1:
        node_counter(node_dict[node][0], result)
    return len(result)


tc = int(input())

for T in range(tc):
    E, N = map(int, input().split())
    node_list = list(map(int, input().split()))
    
    node_dict = defaultdict(list)
    
    for i in range(1, len(node_list), 2):
        node_dict[node_list[i - 1]].append(node_list[i])
    
    total = node_counter(N, [])
    
    print(f"#{T + 1} {total}")