# 5658 . [모의 SW 역량테스트] 보물상자 비밀번호

from collections import deque

tc = int(input())

for T in range(tc):
    n, k = map(int, input().split())
    n_que = deque(map(str, input()))
    size = n // 4  # 한 변에 들어가는 숫자 개수

    num_list = []

    for i in range(size):
        for j in range(4):
            n_str = ''.join(n_que)
            num_list.append(int(n_str[size*j:size*j+size], 16))
        
        n_que.rotate(1)

    n_list_sort = sorted(set(num_list))

    print(f"#{T + 1} {n_list_sort[len(n_list_sort)-k]}")
