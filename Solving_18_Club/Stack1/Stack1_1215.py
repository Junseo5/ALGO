# 1215 . [S/W 문제해결 기본] 3일차 - 회문1

for T in range(10):
    n = int(input())
    size = 8
    n_list = [list(map(str, input())) for _ in range(size)]
    n_list_90 = list(zip(*n_list))

    cnt = 0

    for i in range(size):
        for j in range(n-1, size):
            temp = n_list[i][j-(n-1):j+1]
            reversed_temp = list(reversed(temp))
            if temp == reversed_temp:
                cnt += 1

            temp2 = n_list_90[i][j-(n-1):j+1]
            reversed_temp2 = tuple(reversed(temp2))
            if temp2 == reversed_temp2:
                cnt += 1
    
    print(f"#{T + 1} {cnt}")