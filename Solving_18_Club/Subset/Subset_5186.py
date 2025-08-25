# 5186 . [파이썬 S/W 문제해결 구현] 1일차 - 이진수2

tc = int(input())

for T in range(tc):
    n = float(input())
    
    n_bin = ''
    is_overflow = 'overflow'
    
    for i in range(1, 13):
        if not n:
            is_overflow = n_bin
            break
        
        if 1*(2**(-i)) <= n:
            n_bin += '1'
            n -= 1*(2**(-i))
        else:
            n_bin += '0'
    
    if not n:
        is_overflow = n_bin
    
    
    print(f"#{T + 1} {is_overflow}")