# 2068. 최대수 구하기

tc = int(input())

for T in range(tc):
    n = list(map(int, input().split()))
    
    print(f"#{T+1} {max(n)}")