# 20728 . 공평한 분배 2

tc = int(input())

for T in range(tc):
    n, k = map(int, input().strip().split())
    n_list = list(sorted(map(int, input().strip().split())))
    
    save_min = float('inf')
    
    for i in range(n - k + 1):
        temp = n_list[i + k - 1] - n_list[i]
        
        if temp < save_min:
            save_min = temp
    
    print(f"#{T + 1} {save_min}")