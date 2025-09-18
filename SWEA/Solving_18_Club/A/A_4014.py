# 4014 . [모의 SW 역량테스트] 활주로 건설

def build(n, x, n_list):
    cnt = 0
    for i in range(n):
        stack_list = []
        is_up_down = 'UP'
        temp_num = -1
        is_val = True
        for j in range(n):
            if temp_num != n_list[i][j]:
                if j != 0 and abs(temp_num - n_list[i][j]) >= 2:
                    is_val = False
                    break
                if stack_list:
                    if is_up_down == 'UP':
                        if temp_num < n_list[i][j]:
                            if stack_list[-1] < x:
                                is_val = False
                                break
                        else:
                            is_up_down = 'DOWN'
                    else:
                        if temp_num < n_list[i][j]:
                            if stack_list[-1] < (x * 2):
                                is_val = False
                                break
                            is_up_down = 'UP'
                        else:
                            if stack_list[-1] < x:
                                is_val = False
                                break
                temp_num = n_list[i][j]
                stack_list.append(0)
            
            stack_list[-1] += 1
            
            if j == n - 1 and stack_list[-1] < x:
                if is_up_down == 'DOWN':
                    is_val = False
                    break

        if is_val:
            cnt += 1
    return cnt

tc = int(input())

for T in range(tc):
    n, x = map(int, input().split())
    n_list = [list(map(int, input().split())) for _ in range(n)]
    n_zip_list = list(zip(*n_list))
    
    result = build(n, x, n_list) + build(n, x, n_zip_list)
    
    print(f"#{T + 1} {result}")