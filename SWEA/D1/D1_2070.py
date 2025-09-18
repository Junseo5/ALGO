# 2070. 큰 놈, 작은 놈, 같은 놈

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    
    if n < m:
        print(f"#{T+1} <")
    elif n > m:
        print(f"#{T+1} >")
    else:
        print(f"#{T+1} =")