# 2817 . 부분 수열의 합

import itertools

tc = int(input())

for T in range(tc):
    n, k = map(int, input().split())
    n_list = list(map(int, input().split()))

    cnt = 0

    for i in range(1, n + 1):
        is_big = True
        n_com = itertools.combinations(n_list, i)

        for j_list in n_com:
            j_sum = sum(j_list)
            if j_sum == k:
                cnt += 1
            if j_sum <= k:
                is_big = False

        if is_big:
            break

    print(f"#{T + 1} {cnt}")


# 매우 빠른 최적화된 코드 버전
# from bisect import bisect_left, bisect_right
#
# def count_subseq_equal_k(arr, K):
#     n = len(arr)
#     mid = n // 2
#     L, R = arr[:mid], arr[mid:]
#
#     # 왼쪽/오른쪽 절반의 부분합 전부 만들기
#     sumsL = [0]
#     for v in L:
#         # 기존 리스트를 바로 확장하면 한 턴에 중복되니 새로 만들어 덧붙임
#         sumsL += [s + v for s in sumsL]
#
#     sumsR = [0]
#     for v in R:
#         sumsR += [s + v for s in sumsR]
#
#     # 오른쪽 부분합 정렬 후, 왼쪽의 각 합에 대해 (K - s)을 이분탐색으로 개수 카운트
#     sumsR.sort()
#     cnt = 0
#     for s in sumsL:
#         target = K - s
#         lo = bisect_left(sumsR, target)
#         hi = bisect_right(sumsR, target)
#         cnt += (hi - lo)
#
#     # 공집합(둘 다 0 선택) 제외: 문제에서 "부분 수열(비어있지 않음)" 기준이면 필요
#     if K == 0:
#         cnt -= 1
#
#     return cnt
#
# tc = int(input())
# for T in range(tc):
#     n, k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     # (양수/0만 있다고 가정하는 SWEA 2817 특성상 이 방식이 매우 빠릅니다)
#     ans = count_subseq_equal_k(arr, k)
#     print(f"#{T + 1} {ans}")
