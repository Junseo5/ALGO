# 11592. 크루즈 컨트롤

T = int(input())
for tc in range(1, T + 1):
    D, N = map(int, input().split())

    max_time = 0.0
    for _ in range(N):
        K, S = map(int, input().split())
        max_time = max(max_time, (D - K) / S)

    speed = D / max_time

    print(f"#{tc} {speed:.7f}")
