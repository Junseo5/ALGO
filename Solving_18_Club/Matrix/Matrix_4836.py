# 4836 . [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기

tc = int(input())

for T in range(tc):
    n = int(input())
    n_list = [list(map(int, input().split())) for _ in range(n)]

    base_list = [[0 for _ in range(10)] for _ in range(10)]


    for i in range(n):
        for x in range(n_list[i][0], n_list[i][2] + 1):
            for y in range(n_list[i][1], n_list[i][3] + 1):
                if n_list[i][4] == 1:
                    base_list[x][y] += 1
                elif n_list[i][4] == 2:
                    base_list[x][y] += 2

    cnt = 0

    for i in base_list:
        for j in i:
            if j == 3:
                cnt += 1
    
    print(f"#{T + 1} {cnt}")