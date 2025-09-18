# 1217 . [S/W 문제해결 기본] 4일차 - 거듭 제곱

def power(n, m):
    if m <= 1:
        return n
    
    return n * power(n, m-1)

for T in range(10):
    input() # tc 번호 버리는 값

    n, m = map(int, input().split())

    print(f"#{T + 1} {power(n, m)}")