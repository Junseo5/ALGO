# 16910 . 원 안의 점

result_list = []

tc = int(input())

for T in range(tc):
    n = int(input())
    
    cnt = 0
    
    for i in range(-n, n + 1):
        is_val = False
        for j in range(-n, n + 1):
            if (i ** 2) + (j ** 2) <= n ** 2:
                cnt += 1
                is_val = True
            elif is_val:
                break
    
    result_list.append(f"#{T + 1} {cnt}\n")
    
# 최대한 시간 줄이기 위해 시도해본 최적화
print(''.join(result_list))