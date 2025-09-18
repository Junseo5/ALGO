# 2117 . [모의 SW 역량테스트] 홈 방범 서비스

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    n_list = [list(map(int, input().split())) for _ in range(n)]

    max_house = 0

    for i in range(n):
        for j in range(n):
            for k in range(1, n + 2):
                save_cnt_home = sum(n_list[i][max(0, j - (k - 1)):min(n, (j + (k - 1)) + 1)])
                for l in range(1, k):
                    if 0 <= i - l < n:
                        save_cnt_home += sum(n_list[i - l][max(0, j - ((k - 1) - l)):min(n, (j + ((k - 1) - l)) + 1)])
                    if 0 <= i + l < n:
                        save_cnt_home += sum(n_list[i + l][max(0, j - ((k - 1) - l)):min(n, (j + ((k - 1) - l)) + 1)])

                if (m * save_cnt_home) >= (k * k + (k - 1) * (k - 1)):
                    max_house = max(max_house, save_cnt_home)

    print(f"#{T + 1} {max_house}")