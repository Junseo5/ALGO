# 2071. 평균값 구하기

tc = int(input())

for T in range(tc):
    n = list(map(int, input().split()))
    sum = 0
    
    for i in range(len(n)):
        sum += n[i]
    
    print(f"#{T+1} {round(sum/10)}")