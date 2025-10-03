# 5255 . [파이썬 S/W 문제해결 최적화] 2일차 - 타일 붙이기

dp = [0] * 31
dp[0] = 1
dp[1] = 1
dp[2] = 3

for i in range(3, 31):
    dp[i] = dp[i - 1] + dp[i - 2] * 2 + dp[i - 3]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())

    print(f"#{tc} {dp[n]}")