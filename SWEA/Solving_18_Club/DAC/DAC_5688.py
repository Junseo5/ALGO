# 5688 . 세제곱근을 찾아라

T = int(input())
for tc in range(1, T + 1):
    n = int(input().strip())

    result = -1
    start, end = 0, n
    while start <= end:
        mid = (start + end) // 2
        op = mid ** 3

        if op == n:
            result = mid
            break
        elif op < n:
            start = mid + 1
        else:
            end = mid - 1

    print(f"#{tc} {result}")