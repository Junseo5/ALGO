# 17070. 파이프 옮기기 1

# DFS + 메모이제이션으로 경우의 수 계산
def dfs(r, c, direction):
    # 도착 지점에 파이프 한쪽 끝이 위치할 때 카운트
    if r == n - 1 and c == n - 1:
        return 1

    total = 0

    # 가로 이동: 현재 방향이 가로나 대각선일 때 가능
    if direction == 0 or direction == 2:
        nc = c + 1
        if nc < n and n_list[r][nc] == 0:
            total += dfs(r, nc, 0)

    # 세로 이동: 현재 방향이 세로거나 대각선일 때 가능
    if direction == 1 or direction == 2:
        nr = r + 1
        if nr < n and n_list[nr][c] == 0:
            total += dfs(nr, c, 1)

    # 대각선 이동: 세 칸이 모두 비어 있어야 함
    nr, nc = r + 1, c + 1
    if nr < n and nc < n and n_list[r][nc] == 0 and n_list[nr][c] == 0 and n_list[nr][nc] == 0:
        total += dfs(nr, nc, 2)

    return total


n = int(input())

n_list = [list(map(int, input().split())) for _ in range(n)]

# 시작 상태: (0,1)에서 가로 방향
print(dfs(0, 1, 0))