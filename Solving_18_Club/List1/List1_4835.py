# 4835 . [파이썬 S/W 문제해결 기본] 1일차 - 구간합

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    max_sum = 0
    min_sum = sum(num_list)

    for i in range(n):
        if i <= n-m:  # 인덱스를 벗어나지 않을 때
            temp_sum = sum(num_list[i:i + m])

            max_sum = max(max_sum, temp_sum)
            min_sum = min(min_sum, temp_sum)
    
    print(f"#{T + 1} {max_sum - min_sum}")