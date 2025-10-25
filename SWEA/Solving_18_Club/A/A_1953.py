# 1953 . [모의 SW 역량테스트] 탈주범 검거

from collections import deque

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]
OPP = {0: 2, 1: 3, 2: 0, 3: 1}

tunnel_dict = {
    0: set(),
    1: {0, 1, 2, 3},
    2: {0, 2},
    3: {1, 3},
    4: {0, 1},
    5: {1, 2},
    6: {2, 3},
    7: {0, 3},
}

T = int(input().strip())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    pq = deque()
    visited = [[False] * M for _ in range(N)]
    if board[R][C] == 0:
        print(f"#{tc} 0")
        continue

    pq.append((R, C, 1))
    visited[R][C] = True
    cnt = 1

    while pq:
        r, c, t = pq.popleft()
        if t >= L:
            continue

        now_type = board[r][c]
        for d in tunnel_dict[now_type]:
            nr, nc = r + DR[d], c + DC[d]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if visited[nr][nc]:
                continue
            next_type = board[nr][nc]
            if next_type == 0:
                continue
            if OPP[d] in tunnel_dict[next_type]:
                visited[nr][nc] = True
                cnt += 1
                pq.append((nr, nc, t + 1))

    print(f"#{tc} {cnt}")