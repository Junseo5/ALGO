# 5258 . [파이썬 S/W 문제해결 최적화] 3일차 - 해피박스

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    m_list = [tuple(map(int, input().split())) for _ in range(m)]
    dp = [0] * (n + 1)

    for size, price in m_list:
        for i in range(n, size - 1, -1):
            dp[i] = max(dp[i], dp[i - size] + price)

    print(f"#{tc} {dp[n]}")