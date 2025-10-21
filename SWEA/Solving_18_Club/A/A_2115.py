# A_2115 . 벌꿀채취

T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    seg_list = []
    for r in range(N):
        for c in range(N - M + 1):
            temp_list = board[r][c:c + M]

            total = sum(temp_list)
            if total <= C:
                val = sum(x * x for x in temp_list)
            else:
                best = 0
                for mask in range(1, 1 << M):
                    s = 0
                    sq = 0
                    for i in range(M):
                        if mask & (1 << i):
                            s += temp_list[i]
                            if s > C:
                                break
                            sq += temp_list[i] * temp_list[i]
                    else:
                        if sq > best:
                            best = sq
                val = best

            seg_list.append((r, c, val))

    result = 0
    S = len(seg_list)
    for i in range(S):
        r1, c1, v1 = seg_list[i]
        if v1 == 0:
            continue
        for j in range(i + 1, S):
            r2, c2, v2 = seg_list[j]
            if v2 == 0:
                continue
            if r1 == r2:
                if not (c1 + M <= c2 or c2 + M <= c1):
                    continue
            s = v1 + v2
            if s > result:
                result = s

    print(f"#{tc} {result}")