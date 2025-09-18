# 10505. 소득 불균형

tc = int(input())

for T in range(tc):
    n = int(input())
    score_list = list(map(int, input().split()))
    
    score_avg = sum(score_list) / n
    
    cnt = 0
    for i in range(n):
        if score_list[i] <= score_avg:
            cnt += 1
    
    print(f"#{T + 1} {cnt}")