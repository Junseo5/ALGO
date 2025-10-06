# 4865 . [파이썬 S/W 문제해결 기본] 3일차 - 글자수

from collections import Counter

T = int(input())

for tc in range(1, T + 1):
    str1 = input().strip()
    str2 = input().strip()

    str2_dict = Counter(str2)

    max_num = 0
    for i in str1:
        max_num = max(max_num, str2_dict.get(i, 0))

    print(f"#{tc} {max_num}")