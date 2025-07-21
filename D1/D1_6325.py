# 6325. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 6

l = [2, 4, 6, 8, 10]
print(l)

def foundnum(n, l):
    a = "False"
    for i in range(len(l)):
        if l[i] == n:
            a = "True"
    print(f"{n} => {a}")
            

foundnum(5, l)
foundnum(10, l)