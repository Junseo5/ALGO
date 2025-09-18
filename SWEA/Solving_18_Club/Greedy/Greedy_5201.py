# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    n_list = list(sorted(map(int, input().split()), reverse=True))
    m_list = list(sorted(map(int, input().split())))

    total = 0

    for i in range(m):
        if len(n_list) == 0:
            break

        for j in range(len(n_list)):
            if m_list[i] >= n_list[j]:
                total += n_list[j]
                n_list.pop(j)
                break

    print(f"#{T + 1} {total}")