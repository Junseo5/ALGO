import itertools

tc = int(input())

for T in range(tc):
    n, k_min, k_max = map(int, input().split())
    n_list = list(sorted(map(int, input().split())))
    
    temp = n_list[0]
    temp_idx = 0
    len_list = []
    
    for i in range(1, n):
        if n_list[i] != temp:
            len_list.append(i - temp_idx)
            temp = n_list[i]
            temp_idx = i
    
    len_list.append(n - temp_idx)
    
    result = float("inf")
    
    for i in itertools.product(range(3), repeat=len(len_list)):
        a = b = c = 0
        for l, j in zip(len_list, i):
            if j == 0:
                a += l
            elif j == 1:
                b += l
            else:
                c += l
        
        if k_min <= a <= k_max and k_min <= b <= k_max and k_min <= c <= k_max:
            result = min(result, max(a, b, c) - min(a, b, c))
    
    if result == float('inf'):
        result = -1
    
    print(f"#{T + 1} {result}")