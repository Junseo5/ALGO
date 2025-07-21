# 두 개의 숫자열

tc = int(input())

for i in range(tc):
    n, m = map(int, input().split())
    
    ni = list(map(int, input().split()))
    mi = list(map(int, input().split()))
    
    if n > m:
        ni, mi = mi, ni
        n, m = m, n
        
    final = 0
    
    for j in range(m - n + 1):
        sum = 0
        for k in range(n):
            sum += ni[k] * mi[k + j]
        final = max(final, sum)
    
    print(f"#{i+1} {final}")