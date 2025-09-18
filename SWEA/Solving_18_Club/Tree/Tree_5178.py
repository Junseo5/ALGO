# 5178 . [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합

from collections import defaultdict

tc = int(input())

for T in range(tc):
    N, M, L = map(int, input().split())
    m_tuple_list = [tuple(map(int, input().split())) for _ in range(M)]
    m_dict = defaultdict(list)

    for i in range(1, N + 1):
        left = 2 * i
        right = 2 * i + 1

        if 1 <= left <= N:
            m_dict[i].append([left, 0])
        else:
            m_dict[i].append([0, 0])
        if 1 <= right <= N:
            m_dict[i][0][1] = right

    for key, value in m_tuple_list:
        m_dict[key].append(value)

    for i in range(N, 0, -1):
        if len(m_dict[i]) < 2:
            value = 0
            for j in m_dict[i][0]:
                if j != 0:
                    value += m_dict[j][1]
            m_dict[i].append(value)

    print(f"#{T + 1} {m_dict[L][1]}")