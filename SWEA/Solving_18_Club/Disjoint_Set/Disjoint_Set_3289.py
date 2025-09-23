# 3289 . 서로소 집합

def find(tree, x):
    if tree[x] != x:
        tree[x] = find(tree, tree[x])
    return tree[x]


def union(tree, a_union, b_union):
    a_temp = find(tree, a_union)
    b_temp = find(tree, b_union)

    if a_temp < b_temp:
        tree[b_temp] = a_temp
    else:
        tree[a_temp] = b_temp

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    n_list = [i for i in range(n + 1)]

    result_list = []

    for i in range(m):
        is_find, a, b = map(int, input().split())

        if is_find:
            # for i in range(1, n + 1):
            #     find(n_list, i)
            find(n_list, a)
            find(n_list, b)

            if n_list[a] == n_list[b]:
                result_list.append('1')
            else:
                result_list.append('0')
        else:
            union(n_list, a, b)

    print(f"#{T + 1} {''.join(result_list)}")