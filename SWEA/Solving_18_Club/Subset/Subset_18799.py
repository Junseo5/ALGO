# 18799 . 평균의 평균

import itertools

tc = int(input())

for T in range(tc):
    n = int(input())
    n_list = list(map(float, input().split()))

    ave_save_list = []

    for i in range(1, n + 1):
        n_com = itertools.combinations(n_list, i)

        for j in n_com:
            ave_save_list.append(sum(j) / len(j))

    result = f"{sum(ave_save_list) / len(ave_save_list):.20f}".rstrip('0').rstrip('.')
    print(f"#{T + 1} {result}")