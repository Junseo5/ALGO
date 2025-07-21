# 6329. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 10

def countdown(n):
    if n <= 0:
        print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
    else:
        for i in range(n, 0, -1):
            print(i)
            
countdown(0)
countdown(10)