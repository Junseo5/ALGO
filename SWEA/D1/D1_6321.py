# 6321. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 3

n = int(input())

a = 0

for i in range(1, n+1):
    if n % i == 0:
        a += 1

if a == 2:
    print("소수입니다.")