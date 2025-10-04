# 5215 . 햄버거 다이어트

T = int(input())
for tc in range(1, T + 1):
    n, l = map(int, input().split())
    n_list = [tuple(map(int, input().split())) for _ in range(n)]

    dp = [0] * (l + 1)

    for score, cal in n_list:
        for j in range(l, cal - 1, -1):
            dp[j] = max(dp[j], dp[j - cal] + score)

    print(f"#{tc} {max(dp)}")