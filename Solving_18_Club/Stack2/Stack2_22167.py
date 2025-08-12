# 22167 . [IL lv1 기본기 다지기] 문제 3: 문자열 뒤집기

n = int(input())

for i in range(n):
    n_str = input().strip()

    stack = []

    for j in range(len(n_str)-1, -1, -1):
        stack.append(n_str[j])
    
    print(f"{''.join(stack)}")