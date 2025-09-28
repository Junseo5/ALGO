# 16 섬 찾기

# n*m 격자에 1은 땅 0은 물
# 섬은 땅(1)이 상하좌우 및 대각선으로 연결된 하나 이상의 1로 이루어짐
# 섬의 개수를 찾아라

# 즉, bfs를 dxy로 델타 탐색 돌려서 1이 하나라도 있으면 섬 개수 +1인 것
# 센 섬은 -1 시키고, 1인 섬 기준 델타 확인 후 -1인 섬이 있으면 자신도 -1 = 섬개수 증가 방지

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    dxy = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    cnt = 0
    queue = deque([(0, 0)])
    visited = set((0, 0))
    while queue:
        x, y = queue.popleft()
        
        is_ground = False
        if board[x][y] == 1:
            is_ground = True
        
        is_island = False
        is_val = True
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                
                if is_ground:
                    if board[nx][ny] == -1:
                        is_val = False
                    elif board[nx][ny] == 1:
                        is_island = True
        
        if is_island and is_val:
            cnt += 1
            board[x][y] = -1
        elif not is_val:
            board[x][y] = -1
    
    print(cnt)