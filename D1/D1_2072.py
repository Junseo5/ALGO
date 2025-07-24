# 2072. 홀수만 더하기

T = int(input()) # 5

for i in range(T):
    n = list(map(int, input().split()))
    sum = 0
    
    for j in range(len(n)):
        if n[j] % 2 == 1:
            sum += n[j]
    
    print(f"#{i + 1} {sum}")