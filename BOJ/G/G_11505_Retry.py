# Gold 1 . 11505 구간 곱 구하기 (재시도)

MOD = 1000000007


def init(n, s, e):
    if s == e:
        tree[n] = nums[s]
        return tree[n]

    mid = (s + e) // 2
    tree[n] = (init(n * 2, s, mid) * init(n * 2 + 1, mid + 1, e)) % MOD
    return tree[n]


def update(n, s, e, idx):
    if s > idx or idx > e:
        return tree[n]
    if s == e:
        tree[n] = nums[idx]
        return tree[n]
    mid = (s + e) // 2
    update(n * 2, s, mid, idx)
    update(n * 2 + 1, mid + 1, e, idx)
    tree[n] = tree[n * 2] * tree[n * 2 + 1] % MOD


def find(n, s, e, fs, fe):
    if s > fe or fs > e:
        return 1
    if s == e or (fs <= s and e <= fe):
        return tree[n]
    mid = (s + e) // 2
    return (find(n * 2, s, mid, fs, fe) * find(n * 2 + 1, mid + 1, e, fs, fe)) % MOD


N, M, K = map(int, input().split())
nums = [0] + [int(input()) for _ in range(N)]
tree = [1] * (N * 4)

init(1, 1, N)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        nums[b] = c
        update(1, 1, N, b)
    else:
        print(find(1, 1, N, b, c))