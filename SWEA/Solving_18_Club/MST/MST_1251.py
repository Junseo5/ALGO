# 1251 . [S/W 문제해결 응용] 4일차 - 하나로

import math


class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        self.p[py] = px
        return True


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(n)

    mst_weight = 0
    cnt = 0

    for u, v, weight in edges:
        if uf.union(u, v):
            mst_weight += weight
            cnt += 1
            if cnt == n - 1:
                break

    return mst_weight


tc = int(input())

for T in range(tc):
    n = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    e = float(input())

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            delta_x = x_list[i] - x_list[j]
            delta_y = y_list[i] - y_list[j]
            distance_squared = delta_x ** 2 + delta_y ** 2
            distance = math.sqrt(distance_squared)

            edges.append((i, j, e * (distance ** 2)))

    result = round(kruskal(n, edges))
    print(f"#{T + 1} {result}")