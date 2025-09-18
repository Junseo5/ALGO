# 1244 . [S/W 문제해결 응용] 2일차 - 최대 상금

# 순열 후 k개 만큼 바뀐 값들만 저장 후 max값 출력

tc = int(input())

for T in range(tc):
    n_str, k = input().split()
    n_list = {n_str}
    size = len(n_str)

    for _ in range(int(k)):
        temp_set = set()
        for s in n_list:
            arr = list(s)
            for i in range(size - 1):
                for j in range(i + 1, size):
                    arr[i], arr[j] = arr[j], arr[i]
                    temp_set.add(''.join(arr))
                    arr[i], arr[j] = arr[j], arr[i]
        n_list = temp_set

    print(f"#{T + 1} {max(map(int, n_list))}")