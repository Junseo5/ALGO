# 9490 . 풍선팡

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    n_list = [list(map(int, input().split())) for _ in range(n)]

    total_sum = []

    for i in range(n):
        for j in range(m):
            temp_sum = n_list[i][j]
            for k in range(1, n_list[i][j] + 1):
                if i + k < n:
                    temp_sum += n_list[i + k][j]
                if j + k < m:
                    temp_sum += n_list[i][j + k]
                if i - k >= 0:
                    temp_sum += n_list[i - k][j]
                if j - k >= 0:
                    temp_sum += n_list[i][j - k]
            total_sum.append(temp_sum)
    
    print(f"#{T + 1} {max(total_sum)}")
