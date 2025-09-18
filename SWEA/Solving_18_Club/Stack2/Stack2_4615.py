# 4615 . 재미있는 오셀로 게임

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    xyc = [list(map(int, input().split())) for _ in range(m)]

    board = [[0 for _ in range(n)] for _ in range(n)]

    board[n//2][n//2] = 2
    board[(n//2)][(n//2)-1] = 1
    board[(n//2)-1][(n//2)] = 1
    board[(n//2)-1][(n//2)-1] = 2
    
    # 현재값 기준으로 8방향 탐색을 위한 area 기본값 리스트
    area_list = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(m):
        r_x_loc, r_y_loc, color = xyc[i]
        x_loc = r_x_loc - 1  # 입력 시작값 1, 계산 시작값 0으로 계산값으로 동기화
        y_loc = r_y_loc - 1
        
        board[x_loc][y_loc] = color

        for x_area, y_area in area_list:
            x_idx_area = x_loc + x_area  # 탐색 방향(현재값 주변 8칸) 위치 저장
            y_idx_area = y_loc + y_area
            
            stack = []  # 찾은 방향의 상대방 돌 위치를 저장할 리스트 선언
            
            for j in range(n):
                if 0 <= x_idx_area < n and 0 <= y_idx_area < n:
                    if board[x_idx_area][y_idx_area] == 0:
                        break
                    
                    if board[x_idx_area][y_idx_area] != color:
                        stack.append((x_idx_area, y_idx_area))
                    
                    elif board[x_idx_area][y_idx_area] == color:
                        for temp_x, temp_y in stack:
                            board[temp_x][temp_y] = color
                        break
                    
                    # x_area 변수로 각 방향으로 증가함
                    x_idx_area += x_area
                    y_idx_area += y_area
        
    cnt1 = 0  # 흑돌 카운팅 변수
    cnt2 = 0  # 백돌 카운팅 변수

    for i in board:
        for j in i:
            if j == 1:
                cnt1 += 1
            elif j == 2:
                cnt2 += 1
    
    print(f"#{T + 1} {cnt1} {cnt2}")
