# 21772 . 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전

from collections import deque

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    que = deque(input().split())

    que.rotate(-m)

    print(f"#{T + 1} {que[0]}")