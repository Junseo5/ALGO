# 4864 . [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교

tc = int(input())

for T in range(tc):
    str1 = input()
    str2 = input()

    if str1 in str2:
        num = 1
    else:
        num = 0
    
    print(f"#{T + 1} {num}")