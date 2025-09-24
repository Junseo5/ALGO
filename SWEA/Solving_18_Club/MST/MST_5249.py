# 5249 . [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리

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
    v, e = map(int, input().split())
    e_list = [tuple(map(int, input().split())) for _ in range(e)]

    result = kruskal(v + 1, e_list)
    print(f"#{T + 1} {result}")