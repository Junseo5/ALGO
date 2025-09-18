# 1945 . 간단한 소인수분해

# n = 2**a * 3**b * 5**c * 7**d * 11**e

tc = int(input())

for T in range(tc):
    n = int(input())
    
    total_list = []
    i = 2
    
    while i <= n:
        if n % i == 0:
            total_list.append(i)
            n //= i
            continue
        i += 1
    
    a = total_list.count(2)
    b = total_list.count(3)
    c = total_list.count(5)
    d = total_list.count(7)
    e = total_list.count(11)
    
    print(f"#{T + 1} {a} {b} {c} {d} {e}")