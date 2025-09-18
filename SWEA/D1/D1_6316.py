# 6316. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 9. 내장함수 9

list_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, list_n))))