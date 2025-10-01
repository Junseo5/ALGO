# 5177 . [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙

def heap_insert(heap, value):
    heap.append(value)
    idx = len(heap) - 1
    while idx > 1 and heap[idx] < heap[idx // 2]:
        heap[idx], heap[idx // 2] = heap[idx // 2], heap[idx]
        idx //= 2


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))

    heap = [0]
    for num in nums:
        heap_insert(heap, num)

    idx = n
    total = 0
    while idx > 1:
        idx //= 2
        total += heap[idx]

    print(f"#{tc} {total}")
