# Silver 5 . 1010 다리 놓기

import math

T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    print(math.comb(max(a, b), min(a, b)))