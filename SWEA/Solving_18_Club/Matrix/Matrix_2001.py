# 2001 . 파리 퇴치

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    n_list = [list(map(int, input().split())) for _ in range(n)]

    total_list = []

    for i in range(m-1, n):
        for j in range(m-1, n):
            total = 0
            for x in range(i-m+1, i+1):
                for y in range(j-m+1, j+1):
                    total += n_list[x][y]
            total_list.append(total)

    print(f"#{T + 1} {max(total_list)}")