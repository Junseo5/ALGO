# 2805 . 농작물 수확하기

# 홀수 크기 농장에 수확은 항상 딱맞는 마름모

tc = int(input())

for T in range(tc):
    n = int(input())
    n_list = [list(map(int, input())) for _ in range(n)]
    
    total = 0
    
    for i in range(n):
        for j in range(n):
            if abs(i - (n // 2)) + abs(j - (n // 2)) <= (n // 2):
                total += n_list[i][j]
    
    print(f"#{T + 1} {total}")