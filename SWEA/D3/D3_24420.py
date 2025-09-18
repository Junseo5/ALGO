# 24420. 집합 비교

tc = int(input())

for T in range(tc):
    a, b = map(int, input().split())
    a_set = set(map(int, input().split()))
    b_set = set(map(int, input().split()))
    
    result = '?'
    
    temp = len(a_set & b_set)
    
    if a == b == temp:
        result = '='
    elif a > b and b == temp:
        result = '>'
    elif b > a and a == temp:
        result = '<'
    
    print(result)