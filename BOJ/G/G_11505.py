# Gold 1 . 11505 구간 곱 구하기

# G_2042에서 활용한 버킷 구간 합 세부 관리 기법을 활용하려 하였음
# G_2042를 더욱 빠르게 최적화 가능한 방법
# SIZE = int(math.sqrt(N)) + 1 버킷 크기를 동적으로 1 + 루트N으로 나눠서
# 고정값을 사용하는 것보다 조건도 덜 사용하면서 어떤 수가 나와도
# 가장 빠르고 효율적인 분리 및 계산이 가능하였음
# 하지만 지금 11505 문제는 구간 곱 구하기 문제라 곱셈은 버킷 사용이 불가능
# G_2042와 지금 이 문제 모두 세그먼트 트리 정석 문제였지만 구간 합은 버킷도 사용 가능했음
# 결론, 해당 구간 곱은 세그먼트 트리로 풀어야 한다.

MOD = 1000000007

N, M, K = map(int, input().split())

# 세그먼트 트리 크기 계산 (2^k >= N인 최소 k)
tree_height = 0
temp = N
while temp > 0:
    temp //= 2
    tree_height += 1

tree_size = 1 << (tree_height + 1)  # 2^(height+1)
tree = [1] * tree_size

# 원본 배열
arr = [0] * (N + 1)


# 세그먼트 트리 초기화 (재귀)
def init(node, start, end):
    if start == end:
        arr[start] = int(input())
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    left_val = init(node * 2, start, mid)
    right_val = init(node * 2 + 1, mid + 1, end)
    tree[node] = (left_val * right_val) % MOD
    return tree[node]


# 업데이트: idx번째 수를 val로 변경
def update(node, start, end, idx, val):
    if idx < start or idx > end:
        return tree[node]

    if start == end:
        arr[idx] = val
        tree[node] = val
        return tree[node]

    mid = (start + end) // 2
    left_val = update(node * 2, start, mid, idx, val)
    right_val = update(node * 2 + 1, mid + 1, end, idx, val)
    tree[node] = (left_val * right_val) % 1000000007
    return tree[node]


# 쿼리: [left, right] 구간의 곱
def query(node, start, end, left, right):
    if right < start or left > end:
        return 1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_val = query(node * 2, start, mid, left, right)
    right_val = query(node * 2 + 1, mid + 1, end, left, right)
    return (left_val * right_val) % MOD


# 트리 초기화
init(1, 1, N)

# 쿼리 처리
for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        update(1, 1, N, b, c)
    else:
        print(query(1, 1, N, b, c))