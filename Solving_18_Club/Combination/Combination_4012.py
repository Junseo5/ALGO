# 4012 . [모의 SW 역량테스트] 요리사

import itertools

tc = int(input())

for T in range(tc):
    n = int(input())
    n_list = [list(map(int, input().split())) for _ in range(n)]

    n_idx_list = [i for i in range(n)]

    min_num = float('INF')

    a_com = itertools.combinations(n_idx_list, n//2)

    for i in a_com:
        b_idx_list = []

        for j in n_idx_list:
            if j not in i:
                b_idx_list.append(j)

        a_syn_com = itertools.combinations(i, 2)
        a_syn_sum = 0
        for a in a_syn_com:
            x, y = a
            a_syn_sum += n_list[x][y] + n_list[y][x]

        b_syn_com = itertools.combinations(b_idx_list, 2)
        b_syn_sum = 0
        for b in b_syn_com:
            x, y = b
            b_syn_sum += n_list[x][y] + n_list[y][x]

        min_num = min(min_num, abs(a_syn_sum - b_syn_sum))

    print(f"#{T + 1} {min_num}")