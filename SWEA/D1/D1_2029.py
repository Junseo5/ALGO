# 2029. 몫과 나머지 출력하기

tc = int(input())

for T in range(tc):
    a, b = map(int, input().split())
    
    print(f"#{T+1} {a//b} {a%b}")