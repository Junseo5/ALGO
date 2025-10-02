# 5256 . [파이썬 S/W 문제해결 최적화] 2일차 - 이항계수

N = 70
C = [[0]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    C[i][0] = C[i][i] = 1
    for j in range(1, i):
        C[i][j] = C[i-1][j-1] + C[i-1][j]


T = int(input())
for tc in range(1, T + 1):
    n, a, b = map(int, input().split())

    print(f"#{tc} {C[n][a]}")