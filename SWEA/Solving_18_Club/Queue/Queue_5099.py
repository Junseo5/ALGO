# 5099 . [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기

# 한바퀴 돌 때마다 C//2 줄어들고 0이되면 
# 입력 예제
# 1
# 3 5
# 7 2 6 5 3
# 출력 과정 예제
# 7 2 6 => 3 1 3 => 1 5 1 => 3 2 => 1 1 => 4번째 피자 출력

# deque로 rotate 하면서 맨 앞 값//2 후 확인 및 0 이면 교체
# 두개 만들어서 하나엔 인덱스 넣고 동기화

from collections import deque

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    n_que = deque(map(int, input().split()))

    c_que = deque()
    c_idx_que = deque()

    for i in range(n):
        c_que.append(n_que.popleft())
        c_idx_que.append(i)
    
    while len(c_que) > 1:
        is_val = True
        if c_que[0] > 0:
            c_que[0] //= 2
        
        if c_que[0] == 0:
            c_idx_que.popleft()
            c_que.popleft()
            if n_que:
                c_idx_que.appendleft(m - len(n_que))
                c_que.appendleft(n_que.popleft())
            else:
                is_val = False
        
        if is_val:
            c_que.rotate(-1)
            c_idx_que.rotate(-1)
    
    print(f"#{T + 1} {c_idx_que[0] + 1}")