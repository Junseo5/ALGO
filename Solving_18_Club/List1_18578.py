# 18578 . Gravity_실습

tc = int(input())

for T in range(tc):
    n = int(input())
    boxs = list(map(int, input().split()))

    finally_cnt = 0

    for i in range(n):
        cnt = 0
        for j in range(i + 1, n):
            if boxs[i] > boxs[j]:
                cnt += 1
        finally_cnt = max(finally_cnt, cnt)
        
    print(f"#{T+1} {finally_cnt}")