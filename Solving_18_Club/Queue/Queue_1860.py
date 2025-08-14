# 1860 . 진기의 최고급 붕어빵

# 2 2 2
# 3 4
# 입력받았을 때 n, m, k순으로 2명 2초 후 2개를 만들 수 있다.
# 3초 후 오는 사람 1개 주고 4초 후 오는 사람 1개 주면 가능하다

from collections import deque

tc = int(input())

for T in range(tc):
    n, m, k = map(int, input().split())
    people_que = deque(sorted(map(int, input().split())))

    result = 'Possible'

    for i in range(n):
        # 앞 사람이 가져간 붕어빵을 제외한 현재 남은 개수 계산식
        multi = people_que[0] // m
        stack_cnt = (k * multi) - (n - len(people_que))

        if stack_cnt <= 0:
            result = 'Impossible'
            break
        
        people_que.popleft()
    
    print(f"#{T + 1} {result}")