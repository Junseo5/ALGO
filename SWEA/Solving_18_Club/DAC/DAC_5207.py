# 5207 . [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색

T = int(input().strip())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_list.sort()

    cnt = 0
    for x in b_list:
        l, r = 0, n - 1
        last_dir = 0
        valid = True
        found = False

        while l <= r:
            mid = (l + r) // 2
            if a_list[mid] == x:
                found = True
                break
            elif a_list[mid] < x:
                if last_dir == 1:
                    valid = False
                    break
                last_dir = 1
                l = mid + 1
            else:
                if last_dir == -1:
                    valid = False
                    break
                last_dir = -1
                r = mid - 1

        if found and valid:
            cnt += 1

    print(f"#{tc} {cnt}")
