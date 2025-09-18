# 4843 . [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬

tc = int(input())

for T in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    arr_list = []

    for i in range(5):
        arr_list.append(str(arr[(-i) - 1]))
        arr_list.append(str(arr[i]))

    arr_string = ' '.join(arr_list)

    print(f"#{T + 1} {arr_string}")