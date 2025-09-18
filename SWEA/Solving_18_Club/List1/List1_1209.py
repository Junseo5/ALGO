# 1209 . [S/W 문제해결 기본] 2일차 - Sum

for T in range(10):
    n = int(input())
    n_list = []
    size = 100

    for _ in range(size):
        n_list.append(list(map(int, input().split())))

    left_cross = 0
    right_cross = 0
    total_list = []

    for i in range(size):
        temp1_list = []
        temp2_list = []
        left_cross += n_list[i][i]
        right_cross += n_list[i][size - 1 - i]
        for j in range(size):
            temp1_list.append(n_list[i][j])
            temp2_list.append(n_list[j][i])
        
        total_list.append(sum(temp1_list))
        total_list.append(sum(temp2_list))
    
    total_list.append(left_cross)
    total_list.append(right_cross)

    print(f"#{T + 1} {max(total_list)}")
