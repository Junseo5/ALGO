# 2930 . 힙

import heapq

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    pq = []
    result_list = []

    for _ in range(n):
        n_list = list(map(int, input().split()))

        if n_list[0] == 1:
            heapq.heappush(pq, -n_list[1])
        elif n_list[0] == 2:
            if pq:
                max_num = -heapq.heappop(pq)
                result_list.append(str(max_num))
            else:
                result_list.append(str(-1))

    print(f"#{tc} {' '.join(result_list)}")