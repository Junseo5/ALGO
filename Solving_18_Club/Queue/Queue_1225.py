# 1225 . [S/W 문제해결 기본] 7일차 - 암호생성기

from collections import deque

for T in range(10):
    n = int(input())
    n_que = deque(map(int, input().split()))

    cnt = 1
    
    while n_que[-1] > 0:
        if cnt == 6:
            cnt = 1
        
        n_que[0] -= cnt
        
        n_que.rotate(-1)
        cnt += 1
    
    n_que[-1] = 0
    
    n_list = list(map(str, n_que))

    print(f"#{T + 1} {' '.join(n_list)}")