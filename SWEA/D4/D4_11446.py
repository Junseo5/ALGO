# 11446. 사탕 가방

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))

    bp = 1
    while True:
        total = 0
        for a in n_list:
            total += a // bp
            if total >= M:
                break

        if total >= M:
            bp *= 2
        else:
            break

    left = max(bp // 2, 1)
    right = bp
    result = 0
    while left <= right:
        op = (left + right) // 2

        total = 0
        for a in n_list:
            total += a // op
            if total >= M:
                break

        if total >= M:
            result = op
            left = op + 1
        else:
            right = op - 1

    print(f"#{tc} {result}")
