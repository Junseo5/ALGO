# 6328. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 9

random = list(map(str, input().split(", ")))

for i in range(len(random)):
    if len(random[i]) > len(random[i-1]):
        a = random[i]

print(a)