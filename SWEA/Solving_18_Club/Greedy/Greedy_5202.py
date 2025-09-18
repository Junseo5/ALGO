# 5202 . [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크

tc = int(input())

for T in range(tc):
    n = int(input())
    n_list = [list(map(int, input().split())) for _ in range(n)]
    
    n_list.sort(key=lambda x: x[1])
    
    cnt = 0
    temp = 0
    
    for first, last in n_list:
        if first >= temp:
            cnt += 1
            temp = last
    
    print(f"#{T + 1} {cnt}")