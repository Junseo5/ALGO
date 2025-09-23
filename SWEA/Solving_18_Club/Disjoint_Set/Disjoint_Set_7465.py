# 7465 . 창용 마을 무리의 개수

def find(tree, x):
    if tree[x] != x:
        tree[x] = find(tree, tree[x])
    return tree[x]


def union(tree, a, b):
    a_find = find(tree, a)
    b_find = find(tree, b)

    if a_find < b_find:
        tree[b_find] = a_find
    else:
        tree[a_find] = b_find

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    n_list = [i for i in range(n + 1)]

    for i in range(1, m + 1):
        npc_1, npc_2 = map(int, input().split())
        union(n_list, npc_1, npc_2)

    for i in range(1, n + 1):
        find(n_list, i)

    print(f"#{T + 1} {len(set(n_list)) - 1}")