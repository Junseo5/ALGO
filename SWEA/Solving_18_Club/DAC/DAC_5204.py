# 5204 . [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬


def merge_sort(arr):
    global cnt
    n_len = len(arr)

    if n_len <= 1:
        return arr

    mid = n_len // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    if left_half[-1] > right_half[-1]:
        cnt += 1

    return merge(left_half, right_half)

def merge(left, right):
    result = []

    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result.extend(left[l:])
    result.extend(right[r:])

    return result

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    n_list = list(map(int, input().split()))

    cnt = 0
    n_list = merge_sort(n_list)

    print(f"#{tc} {n_list[n//2]} {cnt}")