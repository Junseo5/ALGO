# 6327. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 8

def square(n):
    print(f"square({n}) => {n*n}")

random = list(map(int, input().split(", ")))

for i in range(len(random)):
    square(random[i])