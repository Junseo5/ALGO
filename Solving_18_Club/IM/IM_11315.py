# 11315 . 오목 판정

# 전체 n을 완전탐색
# 각 현재값 기준 8방향 돌이 있는지 확인
# 없으면 continue 있으면 해당 방향으로 카운팅
# 5개 카운팅 전에 . 나오면 break
# 탐색 중 5개 이상 연속 나오면 break 후 YES 반환

tc = int(input())

for T in range(tc):
    n = int(input())
    board = [list(map(str, input())) for _ in range(n)]
    
    area_list = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    cnt = 1
    result = 'NO'

    for i in range(n):
        if cnt >= 5:
                result = 'YES'
                break
        for j in range(n):
            if cnt >= 5:
                result = 'YES'
                break

            if board[i][j] == '.':
                continue

            for dx, dy in area_list:
                if cnt >= 5:
                    result = 'YES'
                    break
                x_area = i + dx
                y_area = j + dy
                cnt = 1

                for _ in range(4):
                    if 0 <= x_area < n and 0 <= y_area < n:
                        if board[x_area][y_area] != '.':
                            cnt += 1
                        
                        x_area += dx
                        y_area += dy
                    else:
                        break

    print(f"#{T + 1} {result}")