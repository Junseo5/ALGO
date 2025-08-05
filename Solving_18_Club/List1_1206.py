# 1206 . [S/W 문제해결 기본] 1일차 - View

for T in range(10):
    n = int(input())
    boxs = list(map(int, input().split()))

    finally_cnt = []

    for i in range(n-2):
        cnt = []
        for j in range(i - 2, i + 3):
            if i == j:
                continue
            cnt.append(boxs[j])
        
        finally_cnt.append(boxs[i] - max(cnt))
    
    total_sum = 0

    for i in finally_cnt:
        if i > 0:
            total_sum += i

    print(f"#{T+1} {total_sum}")