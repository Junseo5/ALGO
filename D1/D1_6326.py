# 6326. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 7

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        
    print(result)

random = int(input())
factorial(random)
