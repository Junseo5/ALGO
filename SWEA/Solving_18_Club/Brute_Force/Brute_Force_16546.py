# 16546 . Baby-gin_실습

import itertools

tc = int(input())

for T in range(tc):
    n_list = list(map(int, input().strip()))
    
    n_iter = itertools.permutations(n_list, 6)
    
    is_val = 'false'
    
    for n_i in n_iter:
        n_front = n_i[:3]
        n_back = n_i[3:]
        
        run_front = n_front[0] == n_front[1] - 1 == n_front[2] - 2
        run_back = n_back[0] == n_back[1] - 1 == n_back[2] - 2
        triplet_front = n_front[0] == n_front[1] == n_front[2]
        triplet_back = n_back[0] == n_back[1] == n_back[2]
        
        if (run_front or triplet_front) and (run_back or triplet_back):
            is_val = 'true'
            break
    
    print(f"#{T + 1} {is_val}")