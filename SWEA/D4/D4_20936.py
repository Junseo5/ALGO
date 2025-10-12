# 20936. 상자 정렬하기

T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    arr = [None] + a[:] + [0]
    pos = [0] * (N + 1)
    for i in range(1, N+1):
        pos[arr[i]] = i
    empty = N + 1
    moves = []

    def all_fixed():
        for i in range(1, N+1):
            if arr[i] != i:
                return False
        return True

    while not all_fixed():
        misplaced = -1
        for i in range(1, N+1):
            if arr[i] != i:
                misplaced = i
                break

        if empty == N + 1:
            moves.append(misplaced)
            val = arr[misplaced]
            arr[empty] = val
            pos[val] = empty
            arr[misplaced] = 0
            empty = misplaced
        else:
            e = empty
            src = pos[e]
            moves.append(src)
            val = arr[src]
            arr[e] = val
            pos[val] = e
            arr[src] = 0
            empty = src

        if len(moves) > 1500:
            break

    print(len(moves))
    if moves:
        print(*moves)