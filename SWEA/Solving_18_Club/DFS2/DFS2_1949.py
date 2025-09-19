# 1949 . [모의 SW 역량테스트] 등산로 조성

def dfs(x, y, visited, is_k=False, cnt=1):
    global result

    is_val = False
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        loc_num = (nx, ny)

        if 0 <= nx < n and 0 <= ny < n and loc_num not in visited:
            now_num = n_list[x][y]
            if n_list[nx][ny] < now_num:
                visited.add(loc_num)
                dfs(nx, ny, visited, is_k, cnt + 1)
                visited.remove(loc_num)
                is_val = True
            elif (n_list[nx][ny] - k) < now_num and not is_k:
                temp = n_list[nx][ny]
                n_list[nx][ny] = now_num - 1
                is_k = True
                visited.add(loc_num)
                dfs(nx, ny, visited, is_k, cnt + 1)
                visited.remove(loc_num)
                is_k = False
                is_val = True
                n_list[nx][ny] = temp

    if not is_val:
        result = max(result, len(visited))


dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]

tc = int(input())

for T in range(tc):
    n, k = map(int, input().split())
    n_list = [list(map(int, input().split())) for _ in range(n)]

    max_num = max(max(i) for i in n_list)

    result = 0

    for i in range(n):
        for j in range(n):
            if max_num != n_list[i][j]:
                continue

            visited = set()
            visited.add((i, j))
            dfs(i, j, visited)

    print(f"#{T + 1} {result}")