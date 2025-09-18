# 4881 . [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합

import itertools

tc = int(input())

for T in range(tc):
    n = int(input())
    n_list = [list(map(int, input().split())) for _ in range(n)]
    
    n_idx_list = [i for i in range(n)]
    
    n_idx_perm = itertools.permutations(n_idx_list, n)
    
    result_list = []
    save_min = float('inf')
    
    for i in n_idx_perm:
        temp = 0
        for j in range(n):
            temp += n_list[j][i[j]]
            if temp >= save_min:
                break
        
        save_min = min(save_min, temp)
    
    print(f"#{T + 1} {save_min}")