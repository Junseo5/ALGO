# 16268 . 풍선팡2

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    n_list = [list(map(int, input().split())) for _ in range(n)]

    total_sum = []

    for i in range(n):
        for j in range(m):
            temp_sum = n_list[i][j]
            if i + 1 < n:
                temp_sum += n_list[i + 1][j]
            if j + 1 < m:
                temp_sum += n_list[i][j + 1]
            if i - 1 >= 0:
                temp_sum += n_list[i - 1][j]
            if j - 1 >= 0:
                temp_sum += n_list[i][j - 1]
            total_sum.append(temp_sum)
    
    print(f"#{T + 1} {max(total_sum)}")