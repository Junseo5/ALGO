# Gold 1 . 13460 구슬 탈출 2

# 직사각형 N * M, 가작 바깥 둘레는 벽임, 보드에는 구멍 하나 있음
# R, B 구슬 하나씩 들어있음
# 게임 목표는 R 구슬을 구멍 O를 통해 빼내는 것
# 파란 구슬을 O에 들어가면 안됨
# 구슬을 중력을 이용해 동시에 4방향중 하나로 굴린다
# 더 이상 구슬이 움직이지 않을 때 까지 진행
# 최소 몇 번 만에 R 구슬을 구멍으로 빼낼 수 있는지 구하라
#
# 첫 번째 줄 세로 가로 크기 N, M 입력
# 다음 N * M 보드 문자열 입력
# 문자열 텍스트 빈칸'.' 벽'#' 구멍'O' 빨간 구슬'R' 파란 구슬'B'
#
# 만약, 10번 이하로 움직여서 R 구슬 빼낼 수 없으면 -1 출력
#
#
# 구현 아이디어 (실패 이거 아님 BFS 응용임)
# 진행 최대 방향으로 언제나 가중치 1인 다익스트라
# 다익스트라 B부터 진행 위치 갱신 이후 R 진행 B를 벽으로 인식
# '.'만 갈 수 있고, # 방향으로 B만 움직여지면 가중치 1 소모하고 진행

import sys
from collections import deque

# 표준 입력을 빠르게 처리하기 위한 설정
input = sys.stdin.readline

# 보드의 세로(N), 가로(M) 크기 입력
n, m = map(int, input().split())

# 보드 정보 입력
board = []
for i in range(n):
    row = list(input().strip())
    board.append(row)
    # 초기 구슬 위치 찾기
    for j in range(m):
        if row[j] == 'R':
            rx, ry = i, j
        elif row[j] == 'B':
            bx, by = i, j

# 이동 방향 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, d_x, d_y):
    """구슬을 지정된 방향으로 끝까지 이동시키는 함수"""
    move_count = 0
    # 다음 위치가 벽이 아니고, 현재 위치가 구멍이 아닐 때까지 반복
    while board[x + d_x][y + d_y] != '#' and board[x][y] != 'O':
        x += d_x
        y += d_y
        move_count += 1
    return x, y

def bfs():
    """너비 우선 탐색을 통해 최소 이동 횟수를 찾는 함수"""
    # 큐 초기화: (빨간 구슬 x, y, 파란 구슬 x, y, 이동 횟수)
    queue = deque([(rx, ry, bx, by, 0)])
    # 방문 기록을 위한 set: (빨간 구슬 x, y, 파란 구슬 x, y)
    visited = set([(rx, ry, bx, by)])

    while queue:
        r_x, r_y, b_x, b_y, count = queue.popleft()

        # 이동 횟수가 10번을 초과하면 탐색 중단
        if count >= 10:
            continue

        # 네 방향으로 기울이기 시도
        for i in range(4):
            # 빨간 구슬과 파란 구슬 이동
            nrx, nry = move(r_x, r_y, dx[i], dy[i])
            nbx, nby = move(b_x, b_y, dx[i], dy[i])

            # 파란 구슬이 구멍에 빠지면 실패이므로 다른 방향 탐색
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬만 구멍에 빠지면 성공
            if board[nrx][nry] == 'O':
                print(count + 1)
                return

            # 두 구슬의 위치가 겹치는 경우, 위치 조정
            if nrx == nbx and nry == nby:
                # 더 많이 움직인 구슬이 뒤에 있었던 것임
                if abs(nrx - r_x) + abs(nry - r_y) > abs(nbx - b_x) + abs(nby - b_y):
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            # 아직 방문하지 않은 상태라면 큐에 추가하고 방문 처리
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                queue.append((nrx, nry, nbx, nby, count + 1))

    # 10번 안에 성공하지 못하면 -1 출력
    print(-1)

# BFS 함수 실행
bfs()