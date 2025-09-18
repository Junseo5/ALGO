# 4831 . [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

tc = int(input())

for T in range(tc):
    k, n, m = map(int, input().split())
    m_num = list(map(int, input().split()))

    temp = 0
    cnt = 0
    
    for i in range(n+1):
        result = False

        if temp != i:
            continue

        if n <= k + temp:
            break

        for j in range(i + 1, k + i + 1):
            if j in m_num:
                temp = j
                result = True
        
        if not result:
            cnt = 0
            break

        cnt += 1

    print(f"#{T + 1} {cnt}")