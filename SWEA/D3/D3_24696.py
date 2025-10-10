# 24696. 직육면체 자르기

T = int(input())

for tc in range(1, T + 1):
    a, b, c = map(int, input().split())

    if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
        print(1)
    else:
        print(2)