# 4864 . [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교

result_list = []

T = int(input())

for tc in range(1, T + 1):
    n1 = input().strip()
    n2 = input().strip()

    result_list.append(f"#{tc} {0 if n2.find(n1) == -1 else 1}\n")

print(''.join(result_list))