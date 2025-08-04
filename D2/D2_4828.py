# 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max

tc = int(input())

for T in range(tc):
    n = int(input())
    nums = list(map(int, input().split()))

    num_max = nums[0]
    num_min = nums[0]

    for i in nums:
        if num_max < i:
            num_max = i
        elif num_min > i:
            num_min = i
        
    print(f"#{T + 1} {num_max - num_min}")