# 6323. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 4

n = int(input())
list_n = [1]

for i in range(n-1):
    if i == 0:
        list_n.append(list_n[i])
        continue
    list_n.append(list_n[i-1] + list_n[i])

print(list_n)