# 14178. 1차원 정원

tc = int(input())

for T in range(tc):
    n, d = map(int, input().split())
    
    d_area = (d * 2) + 1
    
    if n % d_area == 0:
        result = n // d_area
    else:
        result = (n // d_area) + 1
    
    print(f"#{T + 1} {result}")