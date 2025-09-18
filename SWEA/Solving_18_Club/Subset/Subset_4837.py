# 4837 . [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합

import itertools

total_list = []

tc = int(input())

for T in range(tc):
    n, k = map(int, input().split())
    
    cnt_list = [i for i in range(1, 13)]
    cnt = 0
    
    n_com = itertools.combinations(cnt_list, n)
    
    for i in n_com:
        if sum(i) == k:
            cnt += 1
    
    total_list.append(f"#{T + 1} {cnt}\n")
    
print(''.join(total_list))