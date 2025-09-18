# 9367 . 점점 커지는 당근의 개수

tc = int(input())

for T in range(tc):
    n = int(input())
    n_list = list(map(int, input().split()))
    
    cnt = 1
    max_cnt = 1
    
    for i in range(1, n):
        if n_list[i - 1] < n_list[i]:
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 1
    
    print(f"#{T + 1} {max_cnt}")